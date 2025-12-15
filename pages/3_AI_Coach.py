import streamlit as st
from supabase_client import supabase
from engine.lifestyle_engine import LifestyleEngine

st.set_page_config(page_title="AI Fitness Coach", layout="wide")
st.title("🤖 AI Fitness Coach")

# ---------------- AUTH GUARD ----------------
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔐 Please log in to chat with your AI coach.")
    st.stop()

user = st.session_state.user
engine = LifestyleEngine()
# -------------------------------------------


# ---------------- LOAD CHAT HISTORY ----------------
history_resp = (
    supabase.table("chat_history")
    .select("role, content, created_at")
    .eq("user_id", user.id)
    .order("created_at")
    .execute()
)

chat_history = history_resp.data or []
# --------------------------------------------------


# ---------------- SIDEBAR CONTROLS ----------------
with st.sidebar:
    st.subheader("🗂️ Chat History")
    st.caption("Your past conversations are saved automatically.")

    if st.button("🗑️ Clear Conversation"):
        supabase.table("chat_history").delete().eq("user_id", user.id).execute()
        st.success("Chat history cleared.")
        st.rerun()
# --------------------------------------------------


# ---------------- DISPLAY CHAT (GPT STYLE) --------
for msg in chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
# --------------------------------------------------


# ---------------- CHAT INPUT ----------------------
prompt = st.chat_input("Ask about diet, workouts, recovery, habits...")

if prompt:
    # Save user message
    supabase.table("chat_history").insert({
        "user_id": user.id,
        "role": "user",
        "content": prompt
    }).execute()

    with st.chat_message("user"):
        st.markdown(prompt)

    # Fetch profile
    profile = (
        supabase.table("profiles")
        .select("*")
        .eq("id", user.id)
        .execute()
        .data[0]
    )

    # Fetch recent logs
    logs = (
        supabase.table("daily_logs")
        .select("*")
        .eq("user_id", user.id)
        .order("date", desc=True)
        .limit(7)
        .execute()
        .data
    )

    # Generate AI reply (with memory)
    reply = engine.generate(profile, logs, chat_history, prompt)

    # Save assistant reply
    supabase.table("chat_history").insert({
        "user_id": user.id,
        "role": "assistant",
        "content": reply
    }).execute()

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.rerun()
# --------------------------------------------------



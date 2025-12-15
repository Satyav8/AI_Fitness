import streamlit as st
from datetime import date
from supabase_client import supabase

st.title("📅 Daily Fitness Tracker")

# ---------- AUTH GUARD ----------
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔐 Please log in to access this page.")
    st.stop()

user = st.session_state.user
today = date.today().isoformat()
# --------------------------------


# ---------- SAFE FETCH ----------
response = (
    supabase.table("daily_logs")
    .select("*")
    .eq("user_id", user.id)
    .eq("date", today)
    .maybe_single()
    .execute()
)

data = response.data if response else None
# --------------------------------


# ---------- DEFAULTS ----------
weight = data["weight"] if data else 70.0
calories = data["calories_consumed"] if data else 2000
workout_done = data["workout_done"] if data else False
notes = data["notes"] if data else ""
# --------------------------------


# ---------- INPUTS ----------
weight = st.number_input("⚖️ Weight (kg)", value=float(weight))
calories = st.number_input("🔥 Calories Consumed", value=int(calories))
workout_done = st.checkbox("🏃 Workout Completed", value=workout_done)
notes = st.text_area("📝 Notes", value=notes)
# --------------------------------


# ---------- UPSERT ----------
if st.button("💾 Save Today's Log"):
    supabase.table("daily_logs").upsert(
        {
            "user_id": user.id,
            "date": today,
            "weight": float(weight),
            "calories_consumed": int(calories),
            "workout_done": workout_done,
            "notes": notes,
        },
        on_conflict="user_id,date"
    ).execute()

    st.success("✅ Today's log saved")
# --------------------------------

# -------------------------------------





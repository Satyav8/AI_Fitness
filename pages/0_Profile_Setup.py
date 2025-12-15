import streamlit as st
from supabase_client import supabase

st.title("👤 Profile Setup")

# ---------- AUTH GUARD ----------
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.stop()

user = st.session_state.user
# --------------------------------


# ---------- CHECK IF PROFILE EXISTS ----------
response = (
    supabase.table("profiles")
    .select("*")
    .eq("id", user.id)
    .execute()
)

if response.data and len(response.data) > 0:
    st.success("✅ Profile already set up")
    st.info("➡️ Use the sidebar to continue")
    st.stop()
# --------------------------------------------


st.subheader("Tell us about yourself")

# ---------- PROFILE FORM ----------
height = st.number_input("Height (cm)", value=170.0)
weight = st.number_input("Weight (kg)", value=70.0)
goal = st.selectbox("Goal", ["Lose Fat", "Build Muscle", "Stay Fit"])
activity = st.selectbox("Activity Level", ["Low", "Moderate", "High"])
diet = st.text_input("Diet Preference (optional)")
medical = st.text_area("Medical Conditions (optional)")
# --------------------------------------------


if st.button("💾 Save Profile"):
    supabase.table("profiles").insert({
        "id": user.id,
        "height": float(height),
        "weight": float(weight),
        "goal": goal,
        "activity": activity,
        "diet": diet,
        "medical": medical
    }).execute()

    st.success("🎉 Profile saved successfully!")
    st.rerun()



# --------------------------------

import streamlit as st
from supabase_client import supabase

st.set_page_config(page_title="AI Fitness Coach", layout="wide")

# ---------------- SESSION INIT ----------------
if "user" not in st.session_state:
    st.session_state.user = None

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
# ---------------------------------------------


st.title("🏋️ AI Fitness Coach")

# ================= AUTH FLOW =================
if not st.session_state.authenticated:
    auth_mode = st.radio("Choose action", ["Login", "Sign Up"], horizontal=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # -------- SIGN UP --------
    if auth_mode == "Sign Up":
        if st.button("Create Account"):
            try:
                supabase.auth.sign_up(
                    {"email": email, "password": password}
                )
                st.success("✅ Account created! You can now log in.")
            except Exception as e:
                st.error("❌ Sign-up failed. Email may already exist.")

    # -------- LOGIN --------
    if auth_mode == "Login":
        if st.button("Login"):
            try:
                res = supabase.auth.sign_in_with_password(
                    {"email": email, "password": password}
                )
                st.session_state.user = res.user
                st.session_state.authenticated = True
                st.success("✅ Logged in successfully")
                st.rerun()
            except Exception:
                st.error("❌ Invalid email or password")

    st.stop()
# =============================================


# ================= LOGOUT ====================
with st.sidebar:
    st.success(f"👤 {st.session_state.user.email}")
    if st.button("Logout"):
        st.session_state.user = None
        st.session_state.authenticated = False
        st.rerun()
# =============================================


st.info("➡️ Use the sidebar to navigate between pages")






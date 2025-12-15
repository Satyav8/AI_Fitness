import streamlit as st
import plotly.graph_objs as go
from supabase_client import supabase
from engine.utils import bmi, calorie_target

st.set_page_config(page_title="User Analytics", layout="wide")

# -------------------------
# AUTH CHECK
# -------------------------
user = st.session_state.get("user")
if not user:
    st.error("❌ Please log in to access analytics.")
    st.stop()

st.title("📊 Your Fitness Analytics")
st.caption(f"Hi **{user.email}**, here's your personalized progress dashboard.")
st.markdown("---")

# -------------------------
# FETCH USER PROFILE (SAFE)
# -------------------------
profile_resp = (
    supabase.table("profiles")
    .select("*")
    .eq("id", user.id)
    .execute()
)

if not profile_resp.data:
    st.warning("⚠️ Please complete your profile first.")
    st.stop()

profile = profile_resp.data[0]

height = profile.get("height", 170)
activity = profile.get("activity", "Moderate")
goal = profile.get("goal", "Stay Fit")

# age NOT in DB → safe default
age = 25
# -------------------------


# -------------------------
# FETCH DAILY LOGS
# -------------------------
logs_resp = (
    supabase.table("daily_logs")
    .select("*")
    .eq("user_id", user.id)
    .order("date")
    .execute()
)

logs = logs_resp.data or []

if not logs:
    st.info("📅 No logs yet! Start tracking to see analytics.")
    st.stop()

dates = [log["date"] for log in logs]
weights = [log["weight"] for log in logs]
calories = [log["calories_consumed"] for log in logs]
workouts = [1 if log["workout_done"] else 0 for log in logs]
# -------------------------


# -------------------------
# CALCULATIONS
# -------------------------
current_weight = weights[-1]

bmi_value = bmi(current_weight, height)

cal_target = calorie_target(
    current_weight,
    height,
    age,
    activity
)
# -------------------------


# -------------------------
# BMI CATEGORY
# -------------------------
if bmi_value < 18.5:
    bmi_status, color = "Underweight", "#00BFFF"
elif bmi_value < 25:
    bmi_status, color = "Normal", "#00FF7F"
elif bmi_value < 30:
    bmi_status, color = "Overweight", "#FFD700"
else:
    bmi_status, color = "Obese", "#FF4500"
# -------------------------


# -------------------------
# WORKOUT STREAK
# -------------------------
streak = 0
for done in reversed(workouts):
    if done:
        streak += 1
    else:
        break
# -------------------------


# -------------------------
# TOP METRICS
# -------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("⚖️ Current Weight", f"{current_weight} kg")
col2.metric("📐 BMI", f"{bmi_value}", bmi_status)
col3.metric("🔥 Daily Calorie Target", f"{cal_target} kcal")
col4.metric("🏋️ Workout Streak", f"{streak} days")

st.markdown("---")


# -------------------------
# BMI GAUGE
# -------------------------
bmi_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=bmi_value,
    title={'text': "BMI Score"},
    gauge={
        'axis': {'range': [10, 40]},
        'bar': {'color': color},
        'steps': [
            {'range': [10, 18.5], 'color': "#ADD8E6"},
            {'range': [18.5, 25], 'color': "#90EE90"},
            {'range': [25, 30], 'color': "#FFD580"},
            {'range': [30, 40], 'color': "#FFA07A"}
        ]
    }
))

st.subheader("📐 BMI Overview")
st.plotly_chart(bmi_gauge, use_container_width=True)


# -------------------------
# WEIGHT TREND
# -------------------------
weight_fig = go.Figure()
weight_fig.add_trace(go.Scatter(
    x=dates,
    y=weights,
    mode='lines+markers',
    line=dict(width=3, color="#00eaff"),
    marker=dict(size=8)
))

weight_fig.update_layout(
    title="📈 Weight Progress",
    xaxis_title="Date",
    yaxis_title="Weight (kg)",
    template="plotly_dark"
)

st.plotly_chart(weight_fig, use_container_width=True)


# -------------------------
# CALORIES VS TARGET
# -------------------------
cal_fig = go.Figure()
cal_fig.add_trace(go.Bar(
    x=dates,
    y=calories,
    marker=dict(color="#a100ff"),
    name="Consumed"
))

cal_fig.add_trace(go.Scatter(
    x=dates,
    y=[cal_target] * len(dates),
    mode="lines",
    line=dict(color="#00FF7F", width=2),
    name="Target"
))

cal_fig.update_layout(
    title="🔥 Calorie Intake vs Target",
    xaxis_title="Date",
    yaxis_title="Calories",
    template="plotly_dark"
)

st.plotly_chart(cal_fig, use_container_width=True)


# -------------------------
# WORKOUT ADHERENCE
# -------------------------
workout_fig = go.Figure()
workout_fig.add_trace(go.Bar(
    x=dates,
    y=workouts,
    marker=dict(color="#FFD700")
))

workout_fig.update_layout(
    title="🏋️ Workout Adherence (1 = Done)",
    xaxis_title="Date",
    yaxis=dict(range=[0, 1.2]),
    template="plotly_dark"
)

st.plotly_chart(workout_fig, use_container_width=True)



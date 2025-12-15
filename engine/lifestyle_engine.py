from openai import OpenAI
from dotenv import load_dotenv
import os
from .utils import calorie_target, bmi

load_dotenv()

SYSTEM_PROMPT = """
You are an expert fitness and nutrition coach.

Rules:
- Be practical and actionable
- Personalize advice using user data
- Respect diet preferences and medical conditions
- Give diet + workout guidance together
- Keep responses structured and concise
"""

class LifestyleEngine:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY missing")

        self.client = OpenAI(api_key=api_key)

    def generate(self, profile, logs, chat_history, user_message):
        # ---------- SAFE DEFAULTS ----------
        age = profile.get("age") or 25
        activity = profile.get("activity") or "Moderate"
        goal = profile.get("goal") or "Stay Fit"
        diet = profile.get("diet") or "No preference"
        medical = profile.get("medical") or "None"
        height = profile.get("height", 170)
        weight = profile.get("weight", 70)
        # ----------------------------------

        cal = calorie_target(weight, height, age, activity)
        bmi_value = bmi(weight, height)

        context = f"""
User Profile:
Age: {age}
Weight: {weight}
Height: {height}
BMI: {bmi_value}
Goal: {goal}
Activity Level: {activity}
Diet Preference: {diet}
Medical Conditions: {medical}
Daily Calorie Target: {cal}

Recent Activity Logs:
{logs if logs else "No recent logs"}
"""

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.append({"role": "user", "content": context})

        # Inject previous conversation (last 10 turns)
        for msg in chat_history[-10:]:
            messages.append({"role": msg["role"], "content": msg["content"]})

        messages.append({"role": "user", "content": user_message})

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.4
        )

        return response.choices[0].message.content








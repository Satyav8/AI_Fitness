# 🏋️‍♂️ AI Fitness Coach

### Your Personalized AI-Powered Health Companion

🚀 **Live App:**
👉 [https://aifitness-tk5nypcprxmtqdaj7eflh7.streamlit.app/](https://aifitness-tk5nypcprxmtqdaj7eflh7.streamlit.app/)

---

## 🌟 Overview

**AI Fitness Coach** is a full-stack, production-deployed AI application that delivers **personalized fitness coaching**, **nutrition guidance**, and **progress analytics** using modern AI and cloud technologies.

Unlike generic fitness apps, this platform:

* Adapts to **each user**
* Tracks **daily progress**
* Provides **AI-powered coaching with memory**
* Enforces **enterprise-grade data security**

This is not a demo — it’s a **real, deployed SaaS-style MVP**.

---

## ✨ Key Features

### 🔐 Authentication & Security

* Secure user authentication via **Supabase Auth**
* **Row Level Security (RLS)** ensures complete data isolation
* Each user can access **only their own data**

### 👤 User Profile System

* Personalized profiles (age, height, weight, goals, activity level, diet, medical notes)
* AI recommendations tailored to each individual

### 📅 Daily Fitness Tracker

* Log daily weight
* Track calories consumed
* Record workout completion
* Prevents duplicate entries per day

### 📊 Advanced Analytics Dashboard

* BMI calculation with health category
* Daily calorie target calculation
* Interactive charts (weight, calories, workouts)
* Workout streak tracking
* Visual insights using Plotly

### 🤖 AI Fitness Coach (GPT-Style Chat)

* AI-powered diet & workout guidance
* Context-aware responses
* **Persistent chat history** (like ChatGPT)
* Personalized using:

  * User profile
  * Recent activity logs
  * Conversation history

### ☁️ Cloud Deployed

* Fully deployed on **Streamlit Cloud**
* Scalable, secure, and publicly accessible

---

## 🧠 AI Capabilities

The AI coach:

* Designs meal plans aligned with calorie targets
* Suggests workouts based on fitness level
* Answers fitness, diet, and recovery questions
* Maintains conversational memory
* Adapts advice as the user progresses

Powered by **OpenAI GPT models**.

---

## 🏗️ Tech Stack

| Layer          | Technology                        |
| -------------- | --------------------------------- |
| Frontend       | Streamlit                         |
| Backend        | Python                            |
| Database       | Supabase (PostgreSQL)             |
| Authentication | Supabase Auth                     |
| Security       | Supabase Row Level Security (RLS) |
| AI             | OpenAI API                        |
| Charts         | Plotly                            |
| Deployment     | Streamlit Cloud                   |

---

## 🗂️ Project Structure

```
ai_fitness_coach/
├── app.py
├── pages/
│   ├── 0_Profile_Setup.py
│   ├── 1_Analytics.py
│   ├── 2_Daily_Tracker.py
│   └── 3_AI_Coach.py
├── engine/
│   ├── utils.py
│   └── lifestyle_engine.py
├── supabase_client.py
├── requirements.txt
└── README.md
```

---

## 🔐 Security Architecture

* **Row Level Security enabled** on all tables:

  * `profiles`
  * `daily_logs`
  * `chat_history`
* Policies enforced using:

  ```sql
  auth.uid() = user_id
  ```
* No service role keys exposed
* Secrets managed securely via environment variables

---

## 🚀 Getting Started (Local Setup)

```bash
git clone https://github.com/<your-username>/ai-fitness-coach.git
cd ai-fitness-coach
pip install -r requirements.txt
streamlit run app.py
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_supabase_anon_key
```

---

## 📈 Future Enhancements

* 📱 Mobile app (React Native / Flutter)
* 🏆 Gamification (badges, XP, leaderboards)
* 📧 Weekly AI fitness reports via email
* 💳 Subscription plans (Stripe)
* 🧠 AI usage analytics & cost optimization

---

## 🎯 Why This Project Stands Out

✅ End-to-end full-stack development
✅ Real AI integration with memory
✅ Production deployment
✅ Strong security practices
✅ Scalable architecture

This project demonstrates **practical AI engineering**, **cloud deployment**, and **secure system design** — not just theory.

---

## 👤 Author

**Satya Prabhas**
AI Engineer | Full-Stack Developer | Builder

If you’re a recruiter, judge, or collaborator — feel free to reach out.

---

🔥 **Built. Secured. Deployed.**
This is what modern AI product engineering looks like.

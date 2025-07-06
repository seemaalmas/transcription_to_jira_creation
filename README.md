Here's the updated `README.md` incorporating all your recent changes:

---

# 🧠 LLM-Based Transcript-to-JIRA Task Agent (FastAPI + Streamlit)

This project takes meeting transcripts (`.txt`, `.docx`, `.vtt`) and extracts actionable tasks using an LLM. It then allows you to refine those tasks and create them directly in a JIRA board using the JIRA REST API.

## 📌 Key Features

* Upload and parse transcripts
* Extract and refine actionable tasks using LLaMA 3.2 via Groq
* Create JIRA issues automatically
* Streamlit frontend + FastAPI backend
* Works with JIRA cloud projects (test/dev setup supported)

---

## 📁 Project Structure

```
TRANSCRIPTION_TO_JIRA_CREATION/
├── backend/
│   ├── api.py               # FastAPI app with /extract-refine and /create-jira-task
│   ├── jira_utils.py        # JIRA API logic (token + task creation)
│   ├── prompts.py           # LLM prompt templates
│   ├── task_extractor.py    # Extract tasks using Groq/LLaMA
│   ├── task_refiner.py      # Refine raw tasks into clean list
│   ├── transcript_reader.py # Read .txt, .docx, .vtt files
│   ├── requirements.txt     # Backend dependencies
│
├── frontend/
│   ├── app.py               # Streamlit UI: Upload, Extract, Create JIRA
│   ├── requirements.txt     # Frontend dependencies
│
├── render.yaml              # Render deployment config
├── Dockerfile               # Container for backend
└── README.md                # This file
```

---

## 🚀 Local Setup Instructions

### 🛠 1. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn api:app --reload --port 8000
```

✅ Create `.env` file in the `backend/` folder:

```
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-jira-api-token
JIRA_DOMAIN=your-domain.atlassian.net
JIRA_PROJECT_KEY=YOUR_PROJECT_KEY
```

---

### 🎨 2. Frontend Setup

```bash
cd frontend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

> Make sure the backend is running locally before clicking “Create JIRA Tasks” in the UI.

---

## 🌐 How to Deploy on Render

### 🧩 Backend

1. Push your code to GitHub.
2. On [Render.com](https://render.com), create a new Web Service from your GitHub repo.
3. Set environment variables via the Render dashboard:

   ```
   JIRA_EMAIL=...
   JIRA_API_TOKEN=...
   JIRA_DOMAIN=...
   JIRA_PROJECT_KEY=...
   ```
4. Point the build command to:

   ```
   pip install -r backend/requirements.txt
   ```

   And the start command to:

   ```
   uvicorn backend.api:app --host 0.0.0.0 --port 10000
   ```

### 🌐 Frontend

1. Deploy separately as a Streamlit app.
2. In `frontend/app.py`, **replace `http://localhost:8000`** with your deployed backend URL.

---

## 🧪 How to Create a JIRA Developer Account & Connect

### ✅ Step 1: Create a Free Developer Instance

1. Visit [Atlassian Developer](https://developer.atlassian.com/console/myapps/)
2. Sign in and go to [https://www.atlassian.com/software/jira/free](https://www.atlassian.com/software/jira/free)
3. Set up your test workspace (e.g. `your-instance.atlassian.net`)

### ✅ Step 2: Create a Project

1. Inside JIRA, create a **Scrum Software Project** (e.g., `TAP board`)
2. Note the **Project Key** (e.g. `TAP`) from the board URL

### ✅ Step 3: Create API Token

1. Go to [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Click **Create API token**, name it, and copy it.

### ✅ Step 4: Add Details to `.env`

```bash
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-api-token
JIRA_DOMAIN=your-instance.atlassian.net
JIRA_PROJECT_KEY=TAP
```

> ⚠️ **Ensure the user creating the issue has permission to do so in JIRA** (same email as token).

---

## ✅ Sample Flow

1. Upload transcript → `sample.vtt`
2. Extract tasks → Uses Groq (LLaMA 3.2)
3. Refine tasks → Streamlined bullet points
4. Click "Create JIRA Tasks" → Sends refined list to `/create-jira-task` endpoint
5. Issues get created in JIRA backlog

---

## 🧼 Notes

* Avoid newline characters (`\n`) in `summary` field for JIRA issue creation
* API returns 201 on successful issue creation, 400 on format error
* Create tokens with correct permissions, and never hardcode `.env` in git

---

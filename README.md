# 🧠 LLM-Based Transcript-to-Task Agent (API-Driven)

This project extracts actionable tasks from meeting transcripts (`.txt`, `.docx`, `.vtt`) using LLMs (Groq via OpenAI-compatible API) and serves it via a FastAPI backend + Streamlit frontend.

## 📂 Project Structure

```

AGENT\_POC/
├── backend/
│   ├── api.py                # FastAPI backend
│   ├── prompts.py            # LLM prompts
│   ├── task\_extractor.py     # Extract tasks using Groq LLaMA 3
│   ├── task\_refiner.py       # Refine tasks into clear output
│   ├── transcript\_reader.py  # Load & parse .txt, .docx, .vtt
│   ├── main.py               # Optional local runner
│   ├── requirements.txt      # Backend requirements
│   └── .env                  # Contains GROQ\_API\_KEY
│
├── frontend/
│   ├── app.py                # Streamlit UI
│   ├── requirements.txt      # Frontend requirements
│   └── venv/                 # Frontend virtual environment

````

---

## 🚀 Setup Instructions

### 🔧 1. Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On Mac/Linux

pip install -r requirements.txt
uvicorn backend.api:app --reload --port 8000

If you face issue in local then run below command from root folder
set OPENAI_API_KEY=your-api-key-here
uvicorn backend.api:app --reload

````

✅ Create `.env` in `backend/`:

```env
GROQ_API_KEY=your_groq_api_key
```

---

### 🎨 2. Frontend Setup (Streamlit)

```bash
cd frontend
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On Mac/Linux

pip install -r requirements.txt
streamlit run app.py
```
### 🔹 Step-by-Step

```bash
# 1. Initialize Git
cd AGENT_POC
git init

# 2. Add remote (replace with your GitHub repo URL)
git remote add origin https://github.com/your-username/your-repo-name.git

# 3. Stage all files
git add .

# 4. Commit
git commit -m "Initial commit: Added FastAPI backend and Streamlit frontend for transcript-to-task agent"

# 5. Push to GitHub
git branch -M main
git push -u origin main

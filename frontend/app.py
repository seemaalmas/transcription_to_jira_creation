import streamlit as st
import requests

st.set_page_config(page_title="LLM Task Extractor Agent", layout="centered")
st.title("🤖 Transcript-to-Task Agent")
st.markdown("Upload a `.txt`, `.docx`, or `.vtt` meeting transcript to extract and refine actionable tasks using LLM.")

# Use session state to persist refined tasks
if "refined_tasks" not in st.session_state:
    st.session_state.refined_tasks = []

uploaded_file = st.file_uploader("📂 Upload transcript file", type=["txt", "docx", "vtt"])

# 🔍 Extract tasks API
if uploaded_file and st.button("🔍 Extract Tasks (via API)"):
    with st.spinner("Calling backend API..."):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post("https://transcript-agent-api.onrender.com/extract-refine-from-file", files=files)


        if response.status_code == 200:
            data = response.json()
            st.success("✅ Tasks extracted and refined!")

            st.text_area("📄 Transcript", data["transcript"], height=250)
            st.text_area("📝 Raw Tasks", data["raw_tasks"], height=250)
            st.text_area("✨ Refined Tasks", data["refined_tasks"], height=250)

            # Split refined tasks by line
            tasks = [t for t in data["refined_tasks"].split("\n") if t.strip().startswith("•")]
            st.session_state.refined_tasks = tasks
        else:
            st.error(f"❌ Failed: {response.json()['detail']}")

# ✨ Create JIRA Tasks
if st.session_state.refined_tasks:
    if st.button("🛠️ Create JIRA Tasks"):
        for task in st.session_state.refined_tasks:
            task = task.replace("•", "").strip()
            response = requests.post(
                "https://transcript-agent-api.onrender.com/create-jira-task",
                json={"summary": task[:100], "description": task}
            )
            try:
                json_response = response.json()
                if response.status_code == 200 and "key" in json_response:
                    st.success(f"✅ JIRA Created: {json_response['key']}")
                else:
                    st.error(f"❌ Failed: {response.status_code} - {json_response}")
            except Exception as e:
                st.error(f"❌ Failed to parse response: {str(e)}")

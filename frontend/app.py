import streamlit as st
import requests

st.set_page_config(page_title="LLM Task Extractor Agent", layout="centered")

st.title("🤖 Transcript-to-Task Agent")
st.markdown("Upload a `.txt`, `.docx`, or `.vtt` meeting transcript to extract and refine actionable tasks using LLM.")

uploaded_file = st.file_uploader("📂 Upload transcript file", type=["txt", "docx", "vtt"])

if uploaded_file and st.button("🔍 Extract Tasks (via API)"):
    with st.spinner("Calling backend API..."):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post("http://localhost:8000/extract-refine-from-file", files=files)

        if response.status_code == 200:
            data = response.json()
            st.success("✅ Tasks extracted and refined!")

            st.text_area("📄 Transcript", data["transcript"], height=250)
            st.text_area("📝 Raw Tasks", data["raw_tasks"], height=250)
            st.text_area("✨ Refined Tasks", data["refined_tasks"], height=250)
        else:
            st.error(f"❌ Failed: {response.json()['detail']}")

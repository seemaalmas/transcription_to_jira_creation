from docx import Document
import re

def read_txt(file_obj):
    # FastAPI gives us a file-like object; we read and decode it
    return file_obj.read().decode("utf-8")

def read_docx(file_obj):
    # Load from in-memory file
    doc = Document(file_obj)
    return "\n".join([para.text for para in doc.paragraphs])

def read_vtt(file_obj):
    lines = file_obj.read().decode("utf-8").splitlines()
    content = []
    for line in lines:
        if re.match(r'^\d{2}:\d{2}:\d{2}\.', line) or '-->' in line or line.strip().isdigit():
            continue
        content.append(line.strip())
    return "\n".join([line for line in content if line])

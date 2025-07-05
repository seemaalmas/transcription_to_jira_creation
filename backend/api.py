from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from transcript_reader import read_txt, read_docx, read_vtt
from task_extractor import extract_tasks
from task_refiner import refine_tasks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in prod
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract-refine-from-file")
async def extract_refine_file(file: UploadFile = File(...)):
    try:
        filename = file.filename
        ext = filename.split(".")[-1].lower()

        if ext == "txt":
            content = read_txt(file.file)
        elif ext == "docx":
            content = read_docx(file.file)
        elif ext == "vtt":
            content = read_vtt(file.file)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type.")

        raw_tasks = extract_tasks(content)
        refined_tasks = refine_tasks(raw_tasks)

        return JSONResponse(content={
            "transcript": content,
            "raw_tasks": raw_tasks,
            "refined_tasks": refined_tasks
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


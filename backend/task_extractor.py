from openai import OpenAI
from backend.prompts import TASK_EXTRACTION_PROMPT
import os
from dotenv import load_dotenv
load_dotenv()

# Replace this with your Groq key
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"  # required for Groq
)


def extract_tasks(transcript: str) -> str:
    """
    Takes in a transcript string, sends it to Groq LLM using prompt, returns extracted task list.
    """
    prompt = TASK_EXTRACTION_PROMPT.format(transcript=transcript)

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful AI project assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1000,
    )

    print(response)

    extracted_tasks = response.choices[0].message.content.strip()
    return extracted_tasks

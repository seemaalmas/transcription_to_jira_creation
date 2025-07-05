from openai import OpenAI
from prompts import TASK_REFINEMENT_PROMPT
import os
from dotenv import load_dotenv
load_dotenv()

# Replace this with your Groq key
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"  # required for Groq
)


def refine_tasks(raw_tasks: str) -> str:
    """
    Takes raw tasks as string input, refines and polishes them using Groq LLaMA 3.
    """
    prompt = TASK_REFINEMENT_PROMPT.format(tasks=raw_tasks)

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful AI project assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1000,
    )

    refined_tasks = response.choices[0].message.content.strip()
    return refined_tasks

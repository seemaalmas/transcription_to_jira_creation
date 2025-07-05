# prompts.py

# Prompt to extract raw task descriptions from transcript
TASK_EXTRACTION_PROMPT = """
You are an intelligent project assistant.
Your job is to extract clear, actionable tasks from the transcript of a team meeting.

Instructions:
- Ignore small talk and non-actionable conversations.
- Return only the tasks in bullet-point format.
- If any tasks have owners or due dates mentioned, include that in parentheses.

Transcript:
{transcript}
"""

# Prompt to refine and improve task descriptions
TASK_REFINEMENT_PROMPT = """
You are a helpful assistant tasked with refining a list of raw tasks.
Improve clarity, remove ambiguity, and make sure each task is easy to understand.

Instructions:
- Make each task short, clear, and complete.
- Add inferred context if it's obvious.
- Use consistent formatting.

Tasks:
{tasks}
"""

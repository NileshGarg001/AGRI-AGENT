# workflows/query_flow.py

import json
from langchain_config import llm
from json_storage import read_logs

def query_flow(text: str, user_id: str) -> str:
    """
    Answers a user's question by providing all existing logs to an LLM
    as context (RAG pattern).
    """
    # 1. Retrieve all logs
    logs = read_logs(user_id=user_id)
    if not logs:
        return "⚠️ No logs found. Please log some data first."

    # 2. Create a much more robust RAG prompt
    logs_json_string = json.dumps(logs, indent=2)
    prompt_template = """You are a helpful farm assistant. Your task is to answer the user's question based *only* on the provided data logs.
- First, think step-by-step to analyze the logs and find the relevant information to answer the question.
- Then, provide a clear, friendly, and conversational answer to the user.
- If the answer isn't in the logs, say so. Do not make up information.

Here are the data logs:
{logs_json_string}

Here is the user's question: {question}

Based on the logs, here is the answer:"""
    prompt = prompt_template.format(logs_json_string=logs_json_string, question=text)

    # 3. Get answer from LLM
    answer = llm.invoke(prompt)
    return answer



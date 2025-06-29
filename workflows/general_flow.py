from langchain_config import llm

def general_flow(text: str) -> str:
    """
    Answers a general knowledge question using the base LLM with a helpful persona.
    """
    prompt_template = """You are a helpful farm assistant. Provide a clear and concise answer to the user's question.

User Question: {question}

Answer:"""
    prompt = prompt_template.format(question=text)
    return llm.invoke(prompt)

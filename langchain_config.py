# agri-agent/langchain_config.py
import os
from dotenv import load_dotenv
from langchain_ibm import WatsonxLLM

load_dotenv()
llm = WatsonxLLM(
    model_id="ibm/granite-13b-instruct-v2",
    url=os.getenv("WATSONX_URL"),
    project_id=os.getenv("PROJECT_ID"),
    params={"max_new_tokens": 256, "temperature": 0.0}
)

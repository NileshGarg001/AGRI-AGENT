# workflows/log_flow.py
import json
import datetime as dt
from langchain_config import llm
from json_storage import write_log

def log_flow(text: str) -> str:
    """
    Uses an LLM to extract structured data from a user's natural language
    input and saves it as a JSON log entry.
    """
    # 1. More robust extraction prompt
    prompt_template = '''You are a data entry assistant. From the user's statement, extract the key details into a structured JSON object.

- "action": What did the user do? (e.g., 'harvest', 'sale', 'purchase', 'expense')
- "item": What is the subject of the log? (e.g., 'tomatoes', 'tractor fuel')
- "quantity": A numerical quantity, if mentioned.
- "unit": The unit for the quantity (e.g., 'pounds', 'gallons').
- "value_usd": The monetary value in USD, if mentioned.
- "note": Any other relevant details from the statement.

User statement: {text}
JSON:'''
    prompt = prompt_template.format(text=text)

    # 2. Invoke LLM and parse
    raw_json = llm.invoke(prompt)
    try:
        # The LLM sometimes returns a markdown code block
        if raw_json.startswith("```json"):
            raw_json = raw_json[7:-4].strip()
        data = json.loads(raw_json)
    except json.JSONDecodeError:
        return f"⚠️ Could not parse data from statement. Please be more specific."

    # 3. Add timestamp and persist
    data['timestamp'] = dt.datetime.utcnow().isoformat()
    write_log(data)

    # 4. Return a clean confirmation
    item = data.get('item', 'something')
    action = data.get('action', 'logged')
    return f"✅ Logged: {action.capitalize()} of {item}."

import json
from crewai.tools import tool

@tool
def read_json_tool(file_path: str):
    """
    Read a JSON file from the given file path and return its content as a dictionary.
    Tries to handle encoding errors gracefully.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin1') as f:
            return json.load(f)
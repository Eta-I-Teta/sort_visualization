import json
import subprocess

def read_json_file(way: str) -> json:
    with open(way, "r", encoding="utf-8") as f:
        json_file = json.load(f)
    return json_file

def save_json_file(obj: json, way: str):
    with open(way, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=4, ensure_ascii=False)

def run_python_file(way: str):
    subprocess.run(['python', way])
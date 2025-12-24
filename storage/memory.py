import json
import os

MEMORY_FILE = "data/memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def remember(category, key, value):
    memory = load_memory()
    if category not in memory:
        memory[category] = {}
    memory[category][key] = value
    save_memory(memory)

def recall(key):
    memory = load_memory()
    for category in memory:
        if key in memory[category]:
            return memory[category][key]
    return None

def forget(key):
    memory = load_memory()
    for category in list(memory.keys()):
        if key in memory[category]:
            del memory[category][key]
            if not memory[category]:
                del memory[category]
            save_memory(memory)
            return True
    return False

def summary():
    memory = load_memory()
    result = []
    for category in memory:
        result.extend(memory[category].keys())
    return result

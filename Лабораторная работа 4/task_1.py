# TODO решите задачу
import json
def task() -> float:
    total = 0
    file = open("input.json", "r", encoding="utf-8")
    data = json.load(file)
    file.close()
    for item in data:
        total = total + item["score"] * item["weight"]
    return round(total, 3)
print(task())
import json

with open('variables.json', 'r') as file:
    data = json.load(file)

print("📦 JSON Contents:")
for key, value in data.items():
    print(f"{key}: {value}")

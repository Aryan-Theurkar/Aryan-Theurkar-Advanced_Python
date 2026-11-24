import csv
import json

data = []

with open("input.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        data.append(row)

with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

print("CSV converted into JSON successfully")

import os
import csv
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, "data.csv")
file_path = os.path.join(BASE_DIR, "data.txt")

with open(file_path, "r", encoding="utf8") as file:
    src = json.load(file)

asks = src['asks']

with open(csv_path, "w", encoding="utf8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow([
        "id", "name", "department", "position", "salary", "hire_date"
    ])
    for a in asks:
        writer.writerow(a)

"""
   id = a[0]
    name = a[1]
    department = a[2]
    position = a[3]
    salary = a[4]
    hire_date = a[5]


    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        (
            id,
            name,
            department,
            position,
            salary,
            hire_date
        )
    )
"""


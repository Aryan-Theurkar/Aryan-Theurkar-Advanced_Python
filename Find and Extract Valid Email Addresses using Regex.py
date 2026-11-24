import re

with open("input.txt", "r") as f:
    data = f.read()

pattern = r'[\w.-]+@[\w.-]+\.\w+'

emails = re.findall(pattern, data)

print("Valid Email Addresses:")

for email in emails:
    print(email)

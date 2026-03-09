import re


"""
with open("textfile.txt", "r") as f:
    text = f.read()

används för att öppna en textfil i "read mode".
text-variabeln hamnar i globalt scope och kan nås av kod under
"""

with open("rfc5321.txt", "r") as f:
    text = f.read()

pattern = r"([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})" # r = raw string

# här kan vi hitta alla potentiella e-postadresser från den valda textfilen
results = re.findall(pattern, text)

print(results)
import re

# Räkna ut de 30 vanligaste orden i Romeo och Julia
# med en dictionary

with open("pg1523.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

words = re.findall(r"\b\w+\b", text)

occurrences = {}

for word in words:
    if word not in occurrences:
        occurrences[word] = 1
    else:
        occurrences[word] += 1

res = sorted(occurrences.items(), key=lambda item: item[1], reverse=True)[:30]
print(res)
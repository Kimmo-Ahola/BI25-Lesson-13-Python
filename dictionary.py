import re
import matplotlib.pyplot as plt

# Räkna ut de 30 vanligaste orden i Romeo och Julia
# med en dictionary

with open("romeo_and_juliet.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

words = re.findall(r"\b\w+\b", text)

occurrences = {}

for word in words:
    if word not in occurrences:
        occurrences[word] = 1
    else:
        occurrences[word] += 1

res = sorted(occurrences.items(), key=lambda item: item[1], reverse=True)[:30]

labels = []
values = []

for r in res:
    labels.append(r[0].title())
    values.append(r[1])


plt.bar(labels, values)
plt.title("Most common words in Romeo and Juliet")
plt.xlabel("Word")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.show()


values = [(l/len(words)*100) for l in values]

plt.bar(labels, values)
plt.title("Most common words in Romeo and Juliet")
plt.xlabel("Word")
plt.ylabel("Percentage (%) of all words")
plt.xticks(rotation=90)
plt.show()
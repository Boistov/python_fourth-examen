text = input()

n = {'A': 4, 'E': 3, 'I': 1, 'O': 0, 'U': 0}
text = text.upper()

total = 0
for i in text:
    if i in n:
        total += n[i]
print(total)

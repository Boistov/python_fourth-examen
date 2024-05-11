sentence = input()
har_f = input("any harf netonen sanjed ")

words = sentence.split()

num = []

for word in words:
    i = word.lower().count(har_f.lower())
    num.append(i)

print(num)

"""backward"""
word = []
while True:
    x = input()
    if x == "NULL":
        break
    word.append(x)

for i in reversed(word):
    print(i)

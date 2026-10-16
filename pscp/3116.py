"""school"""
name = input()
first = ord(name[0].upper())
last = ord(name[-1].upper())
password = [first, last - 1, first + 2, last - 3, first + 4, last - 5,\
            first + 6, last - 7, first + 8, last - 9]

for i in range(10):
    password[i] = password[i] % len(name)
    if password[i] >= 10:
        password[i] = str(password[i] % 10)
    else:
        password[i] = str(password[i])
print(" ".join(password[2:8]))

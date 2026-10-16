"""VOWEL"""
laps = int(input())
vowels = 0
for _ in range(laps):
    letter = input().upper()
    if letter in "AEIOU":
        vowels += 1
print(vowels)

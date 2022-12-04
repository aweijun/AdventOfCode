import string
from collections import deque

file = open('input.txt', mode = 'r', encoding = 'utf-8-sig')
lines = deque(file.readlines())
file.close()

alphabets = list(string.ascii_lowercase)
convert_alphabets = {}

for i, a in enumerate(alphabets):
    convert_alphabets[a] = i + 1
    convert_alphabets[a.upper()] = i + 1 + 26

sum = 0

while (lines):
    compartment = lines.popleft().strip()
    compartmentLength= int(len(compartment) / 2)
    overlap = set(compartment[:compartmentLength]).intersection(set(compartment[compartmentLength:]))
    for element in overlap:
        sum = sum + convert_alphabets[element]
print(sum)
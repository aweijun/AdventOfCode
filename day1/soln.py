file = open('input.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()
maxsum = 0
currsum = 0
for line in lines:
    curr = line.strip()
    print(curr)
    if (len(curr) == 0):
        maxsum = max(maxsum, currsum)
        currsum = 0
    else:
        currsum = currsum + int(curr)

print("largest sum", maxsum)
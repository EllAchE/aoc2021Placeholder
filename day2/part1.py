data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

splitList = list(map(lambda a : a.split(), lst))

print(splitList)

vertical = horizontal = 0
for item in splitList:
    if item[0] == "forward":
        horizontal += int(item[1])
    if item[0] == "down":
        vertical -= int(item[1])
    if item[0] == "up":
        vertical += int(item[1])

print(horizontal, vertical)
print(horizontal * vertical)
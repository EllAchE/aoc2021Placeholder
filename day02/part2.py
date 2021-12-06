data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

splitList = list(map(lambda a : a.split(), lst))

vertical = horizontal = aim = 0
for item in splitList:
    if item[0] == "forward":
        horizontal += int(item[1])
        vertical += aim * int(item[1])
    if item[0] == "down":
        aim += int(item[1])
    if item[0] == "up":
        aim -= int(item[1])

print(horizontal, vertical)
print(horizontal * vertical)
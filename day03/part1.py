data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

# count number of lines, then count 0s and 1s in each col and see which is greater
totalLines = len(lst)

charArrayList = list(map(lambda a : list(a), lst))
trackList = [0] * len(charArrayList[0])
print(trackList)

for line in charArrayList:
    for i in range(0, len(line)):
        if line[i] == '0':
            trackList[i] -= 1
        else:
            trackList[i] += 1

print(trackList)
trackList.reverse()
print(trackList)
multiplier = 1
gamma = epsilon = 0
for charCount in trackList:
    if charCount > 0:
        gamma += multiplier * 1
    multiplier *= 2

multiplier = 1
for charCount in trackList:
    if charCount < 0:
        epsilon += multiplier * 1
    multiplier *= 2

print(gamma, epsilon)
print(gamma * epsilon)


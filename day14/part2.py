data = open("input.txt", 'r')
template = data.readline()
data.close()

data = open("input.txt").readlines()
lst = [d.strip() for d in data[2:]]

dictBuild = []
polymerSet = set()
for l in lst:
    line = [i for i in l.split(' -> ')]
    polymerSet.add(line[1])
    dictBuild.append(line)
mapping = dict(dictBuild)

pairCount = dict.copy(mapping)
for key in pairCount:
    pairCount[key] = 0

pairCountClean = dict.copy(pairCount)

for i in range(0, len(template) - 2):
    pair = template[i] + template[i + 1]
    pairCount[pair] = pairCount[pair] + 1

for i in range(0, 40):
    pairCountNew = dict.copy(pairCountClean)
    pairCountNoOverlap = dict.copy(pairCountClean)
    for key in pairCount:
        if pairCount[key] > 0:
            newKey1 = key[0] + mapping[key]
            newKey2 = mapping[key] + key[1]
            pairCountNew[newKey1] += pairCount[key]
            pairCountNew[newKey2] += pairCount[key]
            pairCountNoOverlap[newKey1] += pairCount[key]
    pairCount = pairCountNew

print pairCountNoOverlap

values = set(mapping.values())
counts = {}
for value in values:
    counts[value] = 0

for pair in pairCountNoOverlap:
    for letter in pair:
        counts[letter] += pairCountNoOverlap[pair]
counts[template[-2]] += 1 # last letter is cut off by pairCountNoOverlap

print counts

mostCommon = 0
leastCommon = -1
for key in counts:
    count = counts[key]
    if count > mostCommon:
        mostCommon = count
    if count < leastCommon or leastCommon == -1:
        leastCommon = count

print mostCommon - leastCommon

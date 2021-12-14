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

for i in range(0, 10):
    newTemplate = template[0]
    for i in range(0, len(template) - 1):
        pair = template[i] + template[i+1]
        if pair in mapping:
            newTemplate = newTemplate + mapping[pair] + template[i+1]
    template = newTemplate

mostCommon = 0
leastCommon = len(template)
for polymer in polymerSet:
    polymerCount = template.count(polymer)
    if polymerCount > mostCommon:
        mostCommon = polymerCount
    if polymerCount < leastCommon:
        leastCommon = polymerCount

print mostCommon - leastCommon
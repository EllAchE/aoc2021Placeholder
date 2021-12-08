data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

def splitInputAndOutput(line):
    ioLine = line.split(' | ')
    return {
        "input": ioLine[0].split(),
        "output": ioLine[1].split()
    }

formattedLst = list(map(splitInputAndOutput, lst))

total = 0
outputSet = set()
for line in formattedLst:
    for item in line["output"]:
        if len(item) == 2 or len(item) == 4 or len(item) == 3 or len(item) == 7:
            total += 1
            outputSet.add(item)

print(formattedLst)
print(total)
print(outputSet)

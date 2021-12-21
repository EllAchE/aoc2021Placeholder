data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

graph = {}
smallCaves = {}
for l in lst:
    line = [i for i in l.split('-')]
    if line[0].islower() and not line[0] == "start" and not line[0] == "end":
        smallCaves[line[0]] = False
    if line[1].islower() and not line[1] == "start" and not line[1] == "end":
        smallCaves[line[1]] = False

    if line[0] in graph:
        graph[line[0]].append(line[1])
    else:
        graph[line[0]] = [line[1]]

    if line[1] in graph:
        graph[line[1]].append(line[0])
    else:
        graph[line[1]] = [line[0]]

def countPaths(graph, smallCaves, start, end):
    paths = [0] #pass by ref
    countPathsUtil(graph, smallCaves, start, end, paths, [])
    return paths[0]

def countPathsUtil(graph, smallCaves, start, end, paths, visited):
    if start in smallCaves:
        smallCaves[start] = True
    if start == end:
        paths[0] = paths[0] + 1
        # print [i[0] for i in visited]
    else:
        for i in graph[start]:
            if not i == "start":
                if ([start, i] not in visited and i not in smallCaves) or \
                ([start, i] not in visited and i in smallCaves and not smallCaves[i]):
                    visited.append([start, i])
                    countPathsUtil(graph, smallCaves, i, end, paths, visited)

    if start in smallCaves:
        smallCaves[start] = False
    if len(visited) > 0:
        visited.pop()


print countPaths(graph, smallCaves, "start", "end")

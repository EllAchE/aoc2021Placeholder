data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {'(': 1, '[': 2, '{': 3, '<': 4}

scores = []
for line in lst:
    corrupted = False
    stack = []
    for c in line:
        if c == '(' or c == '[' or c == '{' or c == '<':
            stack.append(c)
        elif dict[stack.pop()] != c:
            corrupted = True
            break
    if not corrupted:
        lineScore = 0
        for s in stack[::-1]:
            lineScore = lineScore * 5
            lineScore = lineScore + points[s]
        scores.append(lineScore)

scores.sort()
print scores[len(scores)/2]

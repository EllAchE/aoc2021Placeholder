data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

total = 0
for line in lst:
    stack = []
    for c in line:
        if c == '(' or c == '[' or c == '{' or c == '<':
            stack.append(c)
        elif dict[stack.pop()] != c:
            total += points[c]
            break

print total

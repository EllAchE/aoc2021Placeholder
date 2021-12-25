from ast import literal_eval
import math

data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]


class Node:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def parseTree(left, right):
    node = Node()
    if left is not None:
        if not isinstance(left, list):
            node.left = Node()
            node.left.data = left
        else:
            node.left = parseTree(left[0], left[1])
    if right is not None:
        if not isinstance(right, list):
            node.right = Node()
            node.right.data = right
        else:
            node.right = parseTree(right[0], right[1])
    return node


def flatTree(flat, root, depth):
    if root is not None:
        flatTree(flat, root.left, depth + 1)
        if root.left is not None and root.left.data is not None:
            flat.append([root.left.data, depth])
        if root.right is not None and root.right.data is not None:
            flat.append([root.right.data, depth])
        flatTree(flat, root.right, depth + 1)
    return flat


def explode(flat):
    for i, f in enumerate(flat):
        if f[1] > 4:
            if i > 0:
                flat[i-1] = [flat[i-1][0] + f[0], flat[i-1][1]]
            if i + 2 < len(flat):
                flat[i+2] = [flat[i+2][0] + flat[i+1][0], flat[i+2][1]]
            flat[i] = [0,4]
            if i + 1 < len(flat):
                flat.pop(i+1)
            return flat, True
    return flat, False


def split(flat):
    for i, f in enumerate(flat):
        if f[0] >= 10:
            leftValue = int(math.floor(float(f[0]) / 2.0))
            rightValue = int(math.ceil(float(f[0]) / 2.0))
            return flat[:i] + [[leftValue, f[1] + 1]] + [[rightValue, f[1] + 1]] + flat[i+1:], True
    return flat, False


def magnitude(flat):
    while len(flat) > 1:
        for i, f in enumerate(flat):
            if i + 1 < len(flat):
                if flat[i+1][1] == f[1]:
                    f[0] = 3*f[0] + 2*flat[i+1][0]
                    f[1] = f[1]-1
                    flat.pop(i + 1)
    return flat[0]

parsedLst = []
for l in lst:
    parsedLst.append(literal_eval(l))

initial = parsedLst[0]
root = parseTree(initial, None)
flat = flatTree([], root, 0)

for add in parsedLst[1:]:
    addTree = parseTree(add, None)
    addFlat = flatTree([], addTree, 0)  # kind of wasteful to parse it in and out of a tree but whatever
    flat = flat + addFlat
    for i in flat:
        i[1] += 1

    while True:
        flat, cont = explode(flat)
        if cont:
            continue
        flat, cont = split(flat)
        if cont:
            continue
        break

print flat
print magnitude(flat)

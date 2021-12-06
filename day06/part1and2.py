data = open("input.txt").readlines()
# copy the data to a list
lst = list(map(lambda a : int(a), data[0].split(',')))

def simpleSoln(days, arr):
    fishMap = {
        "oldFish": {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        },
        "newFish": {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0
        },
    }

    for item in arr:
        fishMap["oldFish"][item] += 1

    while days > 0:
        print(fishMap)
        days -= 1
        fishMap = shiftMap(fishMap)

    print(fishMap)
    print(len(arr))
    total = 0
    for item in fishMap["oldFish"].values():
        total += item
    for item in fishMap["newFish"].values():
        total += item
    print(total)

def shiftMap(oldMap):
    newMap = {
        "oldFish": {},
        "newFish": {}
    }

    newMap["oldFish"][6] = oldMap["newFish"][0] + oldMap["oldFish"][0]
    newMap["oldFish"][5] = oldMap["oldFish"][6]
    newMap["oldFish"][4] = oldMap["oldFish"][5]
    newMap["oldFish"][3] = oldMap["oldFish"][4]
    newMap["oldFish"][2] = oldMap["oldFish"][3]
    newMap["oldFish"][1] = oldMap["oldFish"][2]
    newMap["oldFish"][0] = oldMap["oldFish"][1]

    newMap["newFish"][8] = oldMap["oldFish"][0] + oldMap["newFish"][0]
    newMap["newFish"][7] = oldMap["newFish"][8]
    newMap["newFish"][6] = oldMap["newFish"][7]
    newMap["newFish"][5] = oldMap["newFish"][6]
    newMap["newFish"][4] = oldMap["newFish"][5]
    newMap["newFish"][3] = oldMap["newFish"][4]
    newMap["newFish"][2] = oldMap["newFish"][3]
    newMap["newFish"][1] = oldMap["newFish"][2]
    newMap["newFish"][0] = oldMap["newFish"][1]

    return newMap

simpleSoln(256, lst)
data = open("input.txt").readlines()
# copy the data to a list
binVal = bin(int(data[0],16))[2:].zfill(len(data[0]) * 4)

totalVersion = 0
nextPacket = []


def parsePacket(binValue, packetType, version):
    literal = ''
    if int(packetType, 2) == 4:
        moreDigits = True
        while moreDigits:
            digit = binValue[:5]
            binValue = binValue[5:]
            if int(str(digit)[0]) == 0:
                moreDigits = False
            literal += str(digit)[1:]
        return binValue, 1, int(version, 2), int(literal, 2)
    else:
        lengthType = int(binValue[0], 2)
        binValue = binValue[1:]
        if lengthType == 0:
            totalLength = int(binValue[:15], 2)
            binValue = binValue[15:]
            length = len(binValue)
            totalPackets = 0
            totalVersion = 0

            while totalLength > 0:
                tempPacket = binValue[3:6]
                tempVersion = binValue[:3]
                binValue = binValue[6:]
                b, p, v, l = parsePacket(binValue, tempPacket, tempVersion)
                binValue = b
                totalLength -= length - len(binValue)
                length = len(binValue)
                totalPackets += p
                totalVersion += v

                # I know I should clean this up...
                if int(packetType, 2) == 0:
                    if literal == '':
                        literal = int(l)
                    else:
                        literal += int(l)
                elif int(packetType, 2) == 1:
                    if literal == '':
                        literal = int(l)
                    else:
                        literal *= int(l)
                elif int(packetType, 2) == 2:
                    if literal == '':
                        literal = int(l)
                    elif literal > int(l):
                        literal = int(l)
                elif int(packetType, 2) == 3:
                    if literal == '':
                        literal = int(l)
                    elif literal < int(l):
                        literal = int(l)
                elif int(packetType, 2) == 5:
                    if literal == '':
                        literal = int(l)
                    elif literal > int(l):
                        literal = 1
                    else:
                        literal = 0
                elif int(packetType, 2) == 6:
                    if literal == '':
                        literal = int(l)
                    elif literal < int(l):
                        literal = 1
                    else:
                        literal = 0
                elif int(packetType, 2) == 7:
                    if literal == '':
                        literal = int(l)
                    elif literal == int(l):
                        literal = 1
                    else:
                        literal = 0
            return binValue, 1 + totalPackets, int(version, 2) + totalVersion, literal
        elif lengthType == 1:
            numSubPackets = int(binValue[:11], 2)
            binValue = binValue[11:]
            totalVersion = 0
            while numSubPackets > 0:
                b, p, v, l = parsePacket(binValue[6:], binValue[3:6], binValue[:3])
                binValue = b
                numSubPackets -= 1
                totalVersion += v

                # I know I should clean this up
                if int(packetType, 2) == 0:
                    if literal == '':
                        literal = int(l)
                    else:
                        literal += int(l)
                elif int(packetType, 2) == 1:
                    if literal == '':
                        literal = int(l)
                    else:
                        literal *= int(l)
                elif int(packetType, 2) == 2:
                    if literal == '':
                        literal = int(l)
                    elif literal > int(l):
                        literal = int(l)
                elif int(packetType, 2) == 3:
                    if literal == '':
                        literal = int(l)
                    elif literal < int(l):
                        literal = int(l)
                elif int(packetType, 2) == 5:
                    if literal == '':
                        literal = int(l)
                    elif literal > int(l):
                        literal = 1
                    else:
                        literal = 0
                elif int(packetType, 2) == 6:
                    if literal == '':
                        literal = int(l)
                    elif literal < int(l):
                        literal = 1
                    else:
                        literal = 0
                elif int(packetType, 2) == 7:
                    if literal == '':
                        literal = int(l)
                    elif literal == int(l):
                        literal = 1
                    else:
                        literal = 0
            return binValue, 1 + numSubPackets, int(version, 2) + totalVersion, literal

version = binVal[:3]
packetType = binVal[3:6]
binVal = binVal[6:]

temp1, temp2, temp3, ans = parsePacket(binVal, packetType, version)
print ans
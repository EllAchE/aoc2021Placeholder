data = open("input.txt").readlines()
# copy the data to a list
binVal = bin(int(data[0],16))[2:].zfill(len(data[0]) * 4)

totalVersion = 0
nextPacket = []


# I'm so sorry this code is kind of unreadable
def parsePacket(binValue, packetType, version):
    if int(packetType, 2) == 4:
        moreDigits = True
        while moreDigits:
            digit = binValue[:5]
            binValue = binValue[5:]
            if int(str(digit)[0]) == 0:
                moreDigits = False
        return binValue, 1, int(version, 2)
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
                b, p, v = parsePacket(binValue, tempPacket, tempVersion)
                binValue = b
                totalLength -= length - len(binValue)
                length = len(binValue)
                totalPackets += p
                totalVersion += v
            return binValue, 1 + totalPackets, int(version, 2) + totalVersion
        elif lengthType == 1:
            numSubPackets = int(binValue[:11], 2)
            binValue = binValue[11:]
            totalVersion = 0
            while numSubPackets > 0:
                b, p, v = parsePacket(binValue[6:], binValue[3:6], binValue[:3])
                binValue = b
                numSubPackets -= 1
                totalVersion += v
            return binValue, 1 + numSubPackets, int(version, 2) + totalVersion


version = binVal[:3]
packetType = binVal[3:6]
binVal = binVal[6:]

temp1, temp2, totalVersion = parsePacket(binVal, packetType, version)
print totalVersion
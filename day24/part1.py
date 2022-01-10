data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

def inputCom(wxyz, varOne, initialInteger):
    wxyz[varOne] = initialInteger.pop()

def addCom(wxyz, varOne, varTwo):
    wxyz[varOne] = wxyz[varOne] + varTwo

def mulCom(wxyz, varOne, varTwo):
    wxyz[varOne] = wxyz[varOne] * varTwo

def divCom(wxyz, varOne, varTwo):
    wxyz[varOne] = wxyz[varOne] / varTwo

def modCom(wxyz, varOne, varTwo):
    wxyz[varOne] = wxyz[varOne] % varTwo

def eqlCom(wxyz, varOne, varTwo):
    if wxyz[varOne] == varTwo:
        wxyz[varOne] = 1
    else:
        wxyz[varOne] = 0

def parseInstruction(iptLine, wxyz, monadCode):
    comm = iptLine[:2]
    varOne = iptLine[4]

    if len(iptLine) >= 7:
        if iptLine[6] in ['w', 'x', 'y', 'z']:
            varTwo = wxyz[iptLine[6]]
        else:
            varTwo = int(iptLine[6:])

    if comm == "inp":
         inputCom(wxyz, varOne, monadCode)
    elif comm == "mul":
        mulCom(wxyz, varOne, varTwo)
    elif comm == "add":
        addCom(wxyz, varOne, varTwo)
    elif comm == "eql":
        eqlCom(wxyz, varOne, varTwo)
    elif comm == "div":
        divCom(wxyz, varOne, varTwo)
    elif comm == "mod":
        modCom(wxyz, varOne, varTwo)


initialInteger = [9, 9, 9, 9, 9,
                  9, 9, 9, 9, 9,
                  9, 9, 9, 9]

def checkMonad(monadCode):
    wxyz = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }

    for line in lst:
        parseInstruction(line, wxyz, monadCode)

    if wxyz["z"] == 0:
        return True

import fileinput,sys





variableMap = dict()

def declared(line):
    variableMap[line[2]] = int(line[1])


def eval(line):
    if line[1] in variableMap and line[3] in variableMap:
        if line[2] == '<':
            return variableMap[line[1]] < variableMap[line[3]]
        elif line[2] == '=':
            return variableMap[line[1]] == variableMap[line[3]]
        elif line[2] == '>':
            return variableMap[line[1]] > variableMap[line[3]]
    return "undefined"

for line in fileinput.input():
    parseLine = line.split()
    if len(parseLine) == 3:
        declared(parseLine)
    elif len(parseLine) == 4:
        answer = eval(parseLine)
        if answer == "undefined":
            print("undefined")
        elif answer:
            print("true")
        else:
            print("false")
    sys.stdout.flush()
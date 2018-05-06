import sys





class SecretChamber():
    def __init__(self):
        self.set = dict()
    def add(self, start, end):
        if self.set.get(start) is not None:
            values = self.set.get(start)
            if values is not None and end not in values:
                self.set.get(start).append(end)
        else:
            self.set[start] = [end]

    def find(self, start, end):
        through = [start]
        stack = [start]
        if start == end:
            return True
        while len(stack) != 0:
            temp = self.set.get(stack.pop())
            if temp is not None:
                for element in temp:
                    if element not in through:
                        through.append(element)
                        if element == end:
                            return True
                        else:
                            stack.append(element)
        return False
if __name__ == '__main__':
    num = 0
    translateNum = 0
    testNum = 0
    secretChamber = SecretChamber()    
    for line in sys.stdin:
        if num == 0:
            parse = [int(s) for s in line.split() if s.isdigit()]
            translateNum = parse[0]
            testNum = parse[1]
        else:
            if num < translateNum + 1:
                start = line[0]
                end = line[2]
                secretChamber.add(start, end)
            else:
                line = line.split()
                if len(line[0]) != len(line[1]):
                    print("No")
                else:
                    good = True
                    for i in range(0,len(line[0])):    
                        if not secretChamber.find(line[0][i], line[1][i]):
                            good = False
                            print("No")
                            break
                    if good:
                        print("Yes")

        num += 1


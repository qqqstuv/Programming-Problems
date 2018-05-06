import fileinput

firstLine = True
length = 0
num = 0
array = []
for line in fileinput.input():
    if firstLine:
        firstLine = False
    else:
        if length == 0:
            line = [int(i) for i in line.strip().split(" ")]
            length = line[0]
            num = line[1]
        else:
            partition = [int(i) for i in line.strip().split(" ")]
            array += partition
            # print(num)
            if len(array) == num:
                shortest_distance = 0
                longest_distance = 0
                # print(array)
                for ant in array:
                    shortest_distance = max(shortest_distance, min(ant + 1, length - ant))
                    longest_distance = max(longest_distance, max(length - ant, ant + 1))
                print(shortest_distance, longest_distance)
                array = []
                num = 0
                length = 0
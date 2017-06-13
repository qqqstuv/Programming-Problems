## Simple N Queens problem. Just draw a lot of samples and solution will emerge

## Source: https://open.kattis.com/problems/bishops


import sys

for line in sys.stdin:
    if int(line) == 1:
        print (1)
    else:
        print (int(line) * 2 - 2)

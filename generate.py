

from random import randint

f = open('myfile', 'w')
x = 500
f.write( str(x) + "\n")
for i in range(1, x + 1):
	f.write(str(randint(2,50)) + '\n')
# ('hi there\n')  # python will convert \n to os.linesep
f.close()  # you can omit in most cases as the destructor will call it


import fileinput

order = 0
abc = 0
for line in fileinput.input():
    if order == 0:
    	order = [int(i) for i in line.strip().split(" ")]
    else:
    	abc = line.strip()

order.sort()

# print(abc )
if abc == "ABC":
	pass
elif abc =="ACB":
	order[1], order[2] = order[2], order[1]
elif abc == "BAC":
	order[0], order[1] = order[1], order[0]
elif abc == "BCA":
	pop = order.pop(0)
	order.insert(2,pop)
elif abc == "CAB":
	pop = order.pop()
	order.insert(0,pop)
elif abc == "CBA":
	order = reversed(order)

print( " ".join([str(i) for i in order]))	

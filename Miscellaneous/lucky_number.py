
import fileinput


n = 0
for line in fileinput.input():
	n = int(line.strip())


nums = []
for i in range(1, 10):
	nums.append(i)


def append_val(x):
	ret_list = []
	for i in range(10):
		ret_list.append(x * 10 + i)
	return ret_list


print(nums)
for iteration in range(2, n):
	new_nums = []
	for num in nums:
		new_nums += (append_val(num))
	nums = new_nums
	nums = [x for x in nums if x % iteration == 0]


print(nums)
print("LENGTH ", len(nums))
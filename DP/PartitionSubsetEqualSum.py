


# http://www.techiedelight.com/partition-problem/

class subsetSum(object):
    """docstring for subsetSum"""
    def __init__(self, arg, Sum):
        self.array = arg
        self.sum = Sum
        self.hashMap = dict()

    def recur(self, index, Sumleft):
        # if taking this index means SumLeft is less than 0, then MINSIZE to guarantee not to take it
        # if the index is out of range, then MINSIZE to make sure that there is no way to make this work
        if Sumleft < 0 or index == len(self.array): 
            return False
        if Sumleft == 0:
            return True
        key = str(index) + "|" + str(Sumleft)
        if key in self.hashMap:
            return self.hashMap[key]

        take = self.recur(index + 1, Sumleft - self.array[index])
        notTake = self.recur(index + 1, Sumleft)
        self.hashMap[key] = take or notTake
        return take or notTake

    def hasSubsetSum(self):
        print(self.recur(0, self.sum))



Set = [3,1,1,2,2,1]

totalSum = 0 
for i in Set:
    totalSum += i

if totalSum % 2 == 1:
    print(False)
else:
    subsetSum(Set, totalSum / 2).hasSubsetSum()

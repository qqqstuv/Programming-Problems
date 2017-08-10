import fileinput

class ForestFires(object):    
    trees = [ i for i in range(0,10000)]
    treeList = []

    def getNumber(self, seed):
        return (seed * 5171 + 13297) % 50021

    def realUnion(self, m, n):
        rootN = find(n)
        rootM = find(m)
        self.trees[rootM] = rootN

    def union(self, m):
        adjacent = self.getAdjacent(m)
        for i in adjacent:
            if self.isTree(i):
                self.realUnion(m, i)

    def find(self, m):
        if m != self.trees[m]:
            self.trees[m] = find(self.trees[m])
        return self.trees[m]

    def isTree(self, m):
        return m in self.treeList

    def getAdjacent(self, m):
        x = m // 100
        y = m % 100
        adjacent = []
        if y < 99: # top
            adjacent.append((x * 100) + (y + 1))
        if y > 0:
            adjacent.append((x * 100) + (y - 1))
        if x > 0:
            adjacent.append(((x - 1) * 100) + (y))
        if x < 99:
            adjacent.append(((x + 1) * 100) + (y))
        # print("jon", m, adjacent)
        return adjacent

    def main(self):
        for line in fileinput.input():
            self.trees = [ i for i in range(0,10000)]
            self.treeList = []
            n, seeed = line.split()
            n = int(n)
            seeed = int(seeed)
            i = 0
            count = 0
            r = seeed
            while i <= n:
                r = self.getNumber(r)
                m = r % 10000
                while self.isTree(m):
                    r = self.getNumber(r)
                    m = r % 10000
                self.union(m)
                self.treeList.append(m)
                r = self.getNumber(r)
                A = r % (i + 1)
                r = self.getNumber(r)
                B = r % (i + 1)
                rootA = self.find(self.treeList[A])
                rootB = self.find(self.treeList[B])
                if rootA == rootB:
                    count += 1
                i += 1
                if i % 100 == 0:
                    print (count)
                    count = 0

vaweawe = ForestFires()

vaweawe.main()



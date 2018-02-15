

# Improved by Path Compression and Union By Rank
# Union by rank: set the child of the shallower one
# Path Compression: flatten the tree when called find(): point the parent of node x to the root node
# both find and union runs in O(logn)

class UnionFind:
    """
    Class that implements the union-find structure with
    union by rank and find with path compression
    """
     
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for x in range(n)]
 
    def find(self, v):
        if not v == self.parent[v]:
            self.parent[v] = self.find(self.parent[v]) # path compression
        return self.parent[v]
 
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[xRoot] = yRoot
            if self.rank[xRoot] == self.rank[yRoot]:
                self.rank[yRoot] += 1
 
    def printParent(self):
        print("index: ",list(range(9)))
        print("parent: ", self.parent, sep='')
 
#---------------------------------------------------------------
 
if __name__ == '__main__':
    # Part a)
    uf = UnionFind(9)
    uf.union(2,1)
    uf.union(4,3)
    uf.union(6,5)
    print("\nParent array after union(2,1), union(4,3) and union(6,5):")
    uf.printParent()
 
    # Part b)
    uf.union(2,4)
    print("\nParent array after union(2,1)")
    uf.printParent()
 
    # Part c)
    uf.find(2)
    print("\nParent array after find(2)")
    uf.printParent()
 
    # Part d)
    myDict = {}
    for node in range(9):
        root = uf.find(node)
        if not root in myDict:
            myDict[root] = set([node])
        else:
            myDict[root].add(node)
    print("\nDisjoint sets: ")
    for mySet in myDict.values():
        print(mySet)

import fileinput


parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    cost = 0
    result = []
    for edge in edges:
        weight, vertice1, vertice2 = edge
        
        if find(vertice1) != find(vertice2):
            result.append(sorted([vertice2, vertice1]))
            cost += weight
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    if len(minimum_spanning_tree) != len(graph['vertices']) - 1:
    	print("Impossible")
    	return minimum_spanning_tree
    print(cost)
    result = sorted(result, key=lambda entry: entry[0]) 
    for pair in result:
        print (" ".join(pair))

    return minimum_spanning_tree

edgesCount = 0
vertices = []
edges = []

for line in fileinput.input():
	if line.strip() == "0 0":
		pass
	if edgesCount <= 0:
		edges = []
		vertices, edgesCount = [int(i) for i in line.strip().split(" ")]
		vertices = [str(i) for i in range(vertices)]
		if len(vertices) > 1 and edgesCount == 0:
			edgesCount = 0
			print("Impossible")
			edgesCount = 0

	else:
		edgesCount -= 1
		# print(line)
		line = line.strip().split(" ")
		edges.append((int(line[2]), line[0], line[1]))
		if edgesCount == 0:
			graph = {
			'vertices' : vertices,
			'edges' : set(edges)
			}
			answer =kruskal(graph)
			

#https://leetcode.com/problems/bus-routes/description/
class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        graph = dict()
        idx = 0
        for route in routes:
            for busStop in route:
                if busStop not in graph:
                    graph[busStop] = []
                graph[busStop].append(idx)
            idx += 1
        # print(graph)
        # routes = [set(i) for i in routes]
        queue = [[i,1] for i in graph[S]]
        count = 0
        bus_visited = set()
        sys.stdout.flush()
        while len(queue) != 0:
            bus, time = queue.pop(0)
            if bus in bus_visited:
                continue
            bus_visited.add(bus)
            for busstop in routes[bus]:
                if busstop == T:
                    return time
                for next_bus in graph[busstop]:
                    if next_bus not in bus_visited:
                        queue.append([next_bus, time + 1])
        return -1
            
            
        

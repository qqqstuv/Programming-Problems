def scheduleCourse(self, A):
    pq = []
    start = 0
    for t, end in sorted(A, key = lambda (t, end): end):
        start += t
        heapq.heappush(pq, -t)
        while start > end:
            start += heapq.heappop(pq)
    return len(pq)

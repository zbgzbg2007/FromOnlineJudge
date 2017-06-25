class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        cl = [(c[0], c[1]) for c in courses]
        cl.sort(key=lambda x:x[1])
        pq = []
        start = 0
        for c in cl:
            t, d = c
            start += t
            heapq.heappush(pq, -t)
            if start > d:
                start += heapq.heappop(pq)
        return len(pq)

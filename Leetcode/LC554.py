class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        w, n = sum(wall[0]), len(wall)
        d = dict()
        ans = n
        for i in range(n):
            x = 0
            for j in wall[i]:
                x += j
                d.setdefault(x, 0)
                d[x] += 1
        d[w] = 0
        return n-max(d.values())
            

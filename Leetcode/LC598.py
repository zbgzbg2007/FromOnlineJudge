class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        a, b = m, n
        for op in ops:
            a = min(a, op[0])
            b = min(b, op[1])
        return a*b

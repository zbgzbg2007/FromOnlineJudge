class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        n = len(arrays)
        mi, ma = min(arrays[0]), max(arrays[0])
        ans = 0
        for i in range(1, n):
            x, y = min(arrays[i]), max(arrays[i])
            ans = max(ans, abs(ma-x), abs(mi-y))
            mi = min(mi, x)
            ma = max(ma, y)
        return ans
        

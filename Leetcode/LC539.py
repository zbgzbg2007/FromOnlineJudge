class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        times = []
        for s in timePoints:
            a1, a2 = int(s[0:2]), int(s[3:5])
            times.append(a1 * 60 + a2)
        ans = 1440
        times = sorted(times)
        n = len(times)
        for i in range(n):
            x = min(abs(times[i]-times[i-1]), 1440-abs(times[i]-times[i-1]))
            ans = min(x, ans)
        
        return ans

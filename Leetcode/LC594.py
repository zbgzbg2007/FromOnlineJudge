class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.Counter(nums)
        ans = 0
        for i in d:
            if i+1 in d:
                ans = max(d[i]+d[i+1], ans)
        return ans

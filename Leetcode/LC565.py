class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, n = 0, len(nums)
        seen = [False] * n
        for i in range(n):
            s = 0
            j = nums[i]
            while seen[j] == False:
                s += 1
                seen[j] = True
                j = nums[j]
            ans = max(ans, s)
        return ans

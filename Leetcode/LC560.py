class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        index = dict()
        ans, s, n = 0, 0, len(nums)
        index[0] = 1
        for i in range(n):
            s += nums[i]
            ans += index.get(s-k, 0)
            index.setdefault(s, 0)
            index[s] += 1
        return ans
            

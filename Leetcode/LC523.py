class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sums = {}
        s = 0
        if k == 0:
            n, i = len(nums), 0
            while i < n - 1:
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
                i += 1
            return False
        for j, i in enumerate(nums):
            s += i
            x = s % k
            if (x in sums and j - sums[x] > 1) or (x == 0 and j > 0):
                return True
            elif x not in sums:
                sums[x] = j
        return False

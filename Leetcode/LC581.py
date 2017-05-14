class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = sorted(nums)
        a, b = 1, 0
        for i, j in enumerate(x):
            if j != nums[i]:
                a = i
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != x[i]:
                b = i
                break
        return b-a+1

class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def split(nums):
            total = sum(nums)
            A = [nums[i] for i in range(len(nums))]
            for i in range(1, len(nums)):
                A[i] += A[i-1]
            return {A[i-1] for i in range(1, len(nums)) if A[i-1] == total - A[i]}
        
        return any(split(nums[:j]) & split(nums[j+1:]) for j in range(3, len(nums)-3))
    

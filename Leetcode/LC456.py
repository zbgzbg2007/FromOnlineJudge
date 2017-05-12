class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = []
        s3 = None
        for i in range(len(nums)-1, -1, -1):
            if s3 is not None and nums[i] < s3:
                return True
            while s and nums[i] > s[-1]:
                s3 = s.pop()
            s.append(nums[i])    
        return False
                

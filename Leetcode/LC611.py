class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        nums.sort()
        for i in range(n):
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    ans += r-l
                    r -= 1
                else:
                    l += 1
        return ans
            

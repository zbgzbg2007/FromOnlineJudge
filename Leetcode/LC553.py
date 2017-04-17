class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        ans = self.f(nums, 0, len(nums)-1) 
        return ans[1]
        
    def f(self, nums, start, end):
        # return a tuple of (max, str_max, min, str_min)
        if start == end:
            ma, mi = float(nums[start]), float(nums[start])
            str_ma, str_mi = str(nums[start]), str(nums[start])
            return (ma, str_ma, mi, str_mi)
        ma, mi = 0., nums[start]+1.
        str_ma, str_mi = '', ''
        for i in range(start, end):
            l = self.f(nums, start, i)
            r = self.f(nums, i+1, end)
            if i == end-1:
                x1, x2 = '/', ''
            else:
                x1, x2 = '/(', ')'
            if ma < (l[0]/r[2]):
                ma = l[0]/r[2]
                str_ma = l[1]+x1+r[3]+x2
            if mi > (l[2]/r[0]):
                mi = l[2]/r[0]
                str_mi = l[3]+x1+r[1]+x2
        return (ma, str_ma, mi, str_mi)
            
            

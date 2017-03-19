class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        rounds = 1
        while n != 2**rounds:
            rounds += 1
        ans = [1]
        for i in range(1, rounds+1, 1):
            temp = [0 for j in range(2**i)]
            x = 2**i + 1
            for j in range(len(ans)):
                temp[2*j] = ans[j]
                temp[2*j+1] = x - ans[j]
            ans = temp
        return self.combine(rounds, ans)
        
    def combine(self, n, nums):
        if n == 0:
            return ''
        if n == 1:
            return '('+str(nums[0])+','+str(nums[1])+')'
        
        a = self.combine(n-1, nums[:2**(n-1)])
        b = self.combine(n-1, nums[2**(n-1):])
        return '('+a+','+b+')'
        

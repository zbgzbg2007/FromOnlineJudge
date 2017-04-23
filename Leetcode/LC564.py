class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        nums = [10**(len(n)-1)-1, 10**(len(n))+1, 10**(len(n))-1, 10**(len(n)-1)+1]
        
        x = list(n)
        pre = int(n[:(len(n)+1)/2])
        for i in [pre+1, pre-1, pre]:
            if len(n)%2 == 0:
                nums.append(int(str(i)+str(i)[::-1]))
            else:
                nums.append(int(str(i)+str(i)[::-1][1:]))
        x = int(n)
        d, ans = x*100, 0
        for i in nums:
            if i != x and (abs(i-x) < d or (abs(i-x) == d and i < ans)):
                ans = i
                d = abs(i-x)
        return str(ans)

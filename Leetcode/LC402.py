class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        s = []
        for i in num:
            while s and s[-1] > i and k > 0:
                s.pop()
                k -= 1
            if i != '0' or (s and i == '0'):
                s.append(i)
        ans = ''.join(s[:-k]) if k != 0 else ''.join(s)
        if ans == '': ans = '0'
        return ans

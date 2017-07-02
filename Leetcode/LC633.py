class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int((c/2)**0.5)+1):
            x = c - i*i
            if x == int(x**0.5)**2:
                return True
        return False

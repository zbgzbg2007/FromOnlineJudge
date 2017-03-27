class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        left = num - 1
        n = int(num**0.5)
        for i in range(2, n+1):
            if num % i == 0:
                left -= i + num / i
                if left < 0:
                    return False
        if left != 0:
            return False
        return True

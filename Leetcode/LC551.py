class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a, l = 0, 0
        for i in s:
            if i == 'A':
                a += 1
            if a > 1:
                return False
        if s.find('LLL') != -1:
            return False
        return True

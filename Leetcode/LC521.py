class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) > len(b):
            return len(a)
        if len(b) > len(a):
            return len(b)
        if a == b:
            return -1
        return len(a)
        

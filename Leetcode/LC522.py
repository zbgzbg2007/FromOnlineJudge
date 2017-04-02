class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def subseq(a, b):
            b = iter(b)
            return all(c in b for c in a)
        strs.sort(key=len, reverse=True)
        for s in strs:
            if sum(subseq(s, t) for t in strs) == 1:
                return len(s)
        return -1
                
        

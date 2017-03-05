class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        ans = 0
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        res = set()
        for i in nums:
            mydict[i] -= 1
            if mydict.get(i + k, 0) != 0:
                res.add((i, i + k))
            if mydict.get(i - k, 0) != 0:
                res.add((i - k, i))
            mydict[i] += 1
        return len(res)
            
                

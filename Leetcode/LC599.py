class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d2 = {x: i for i, x in enumerate(list2)}
        ans = len(list1)+len(list2)
        res = []
        for i, r in enumerate(list1):
            if r in d2:
                if ans > i+d2[r]:
                    res = [r]
                    ans = i+d2[r]
                elif ans == i+d2[r]:
                    res.append(r)
        return res
                
                

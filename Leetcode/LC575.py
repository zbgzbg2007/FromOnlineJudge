class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        num = len(candies)
        x = set()
        for i in candies:
            x.add(i)
        if num >= 2*len(x):
            return len(x)
        return num/2

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        m = n
        n = len(flowerbed)
        for i in range(0, n):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1] == 0) and (i == n-1 or flowerbed[i+1] ==0):
                flowerbed[i] = 1
                m -= 1
        if m > 0:
            return False
        return True
                

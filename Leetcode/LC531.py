class Solution(object):
   def findLonelyPixel(self, picture):
       """
       :type picture: List[List[str]]
       :rtype: int
       """
       ans = 0
       n, m = len(picture), len(picture[0])
       row = [0 for i in range(n)]
       col = [0 for j in range(m)]
       for i in range(n):
           for j in range(m):
               if picture[i][j] == 'B':
                   row[i] += 1
                   col[j] += 1
       for i in range(n):
           for j in range(m):
               if picture[i][j] == 'B' and row[i] == 1 and col[j] == 1:
                   ans += 1
       return ans

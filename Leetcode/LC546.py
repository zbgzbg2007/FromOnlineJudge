class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)
        dp = [[[-1 for i in range(n)] for j in range(n)] for k in range(n)]
        # dp[i][j][k] stores the max points we can get from boxes[i] to boxes[j] with additional k same boxes of 
        # value boxes[j] on the right of boxes[j] 
        return self.f(boxes, dp, 0, n-1, 0)
        
    def f(self, boxes, dp, i, j, k):
        if i > j:
            return 0
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        dp[i][j][k] = self.f(boxes, dp, i, j-1, 0) + (k+1)**2
        x = j-1
        while x >= i:
            if boxes[x] == boxes[j]:
                y = x-1
                while boxes[y] == boxes[j] and y >= i:
                    y -= 1
                y += 1
                z = self.f(boxes, dp, i, y, k+x-y+1) + self.f(boxes, dp, x+1, j-1, 0)
                dp[i][j][k] = max(dp[i][j][k], z)
                x = y-1
            else:
                x -= 1
            
        return dp[i][j][k]
                

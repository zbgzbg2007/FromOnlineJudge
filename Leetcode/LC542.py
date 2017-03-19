import Queue
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(matrix), len(matrix[0])
        ans = [[m+n+4 for i in range(m)] for j in range(n)]
        q = Queue.Queue()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    ans[i][j] = 0
                    q.put((i, j))
        while q.empty() == False:
            i, j = q.get()
            x = ans[i][j] + 1
            if i-1 >=0 and ans[i-1][j] > x:
                ans[i-1][j] = x
                q.put((i-1, j))
            if j-1 >=0 and ans[i][j-1] > x:
                ans[i][j-1] = x
                q.put((i, j-1))
            if i+1 < n and ans[i+1][j] > x:
                ans[i+1][j] = x
                q.put((i+1, j))
            if j+1 < m and ans[i][j+1] > x:
                ans[i][j+1] = x
                q.put((i, j+1))
        return ans
                
            

class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M: return 0
        n, m = len(M), len(M[0])
        A = [[[0 for k in range(4)] for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if M[i][j] == 1:
                    A[i][j][0] = A[i][j-1][0] + 1 
                    A[i][j][1] = A[i-1][j][1] + 1 
                    A[i][j][2] = A[i-1][j-1][2] + 1 if j-1 >= 0 else 1
                    A[i][j][3] = A[i-1][j+1][3] + 1 if j+1 < m else 1
        return max([max([max(A[i][j]) for j in range(m)]) for i in range(n)])

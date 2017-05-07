class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        w = [[0 for a in range(n+2)] for b in range(m+2)]
        ans = 0
        w[i+1][j+1] = 1
        z = 10**9 + 7
        for _ in range(N):
            x = [[0 for a in range(n+2)] for b in range(m+2)]
            for a in range(1, m+1):
                for b in range(1, n+1):
                    for c, d in ((a-1, b), (a+1, b), (a, b-1), (a, b+1)):
                        if c == 0 or d == 0 or c == m+1 or d == n+1:
                            ans += w[a][b]
                        else: 
                            x[c][d] += (w[a][b] % z)
            w = x
        return ans % z

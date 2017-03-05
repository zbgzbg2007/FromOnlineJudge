class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        n, m = len(picture), len(picture[0])
        row = [0 for i in range(n)]
        col = [0 for j in range(m)]
        for i in range(n):
            for j in range(m):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
        same = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if picture[i] == picture[j]:
                    same[i][j] = True
        same_row = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if same[i][j] == True:
                    same_row[i] += 1
        ans = 0
        for j in range(m):
            if col[j] == N:
                for i in range(n):
                    if same_row[i] == N and picture[i][j] == 'B' and row[i] == N:
                        ans += N
                        break
        return ans
                        

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        flag = True
        if len(matrix) == 0: return []
        m, n = len(matrix), len(matrix[0])
        ans = []
        i, j = 0, 0
        while len(ans) < m*n:
            ans.append(matrix[i][j])
            if flag:
                i -= 1
                j += 1
                if i < 0 or j >= n: flag = False
                if j >= n: 
                    j = n-1 
                    i += 2
                elif i < 0: i = 0
            else:
                i += 1
                j -= 1
                if i >= m or j < 0: flag = True
                if i >= m: 
                    i = m-1
                    j += 2
                elif j < 0: j = 0
        return ans

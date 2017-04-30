class Solution1(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r <= 0 or c <= 0:
            return nums
        n, m = len(nums), len(nums[0])
        if r * c != m * n:
            return nums
        ans = [[0 for j in range(c)] for i in range(r)]
        for i in range(m*n):
            ans[i/c][i%c] = nums[i/m][i%m]
        return ans
            
            
class Solution2(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r <= 0 or c <= 0:
            return nums
        n, m = len(nums), len(nums[0])
        if r * c != m * n:
            return nums
        ans = [[0 for j in range(c)] for i in range(r)]
        i, j, x, y = 0, 0, 0, 0
        while i < n:
            ans[x][y] = nums[i][j]
            if j == m-1:
                i, j = i+1, 0
            else:
                j += 1
            if y == c-1:
                x, y = x+1, 0
            else:
                y += 1
        return ans
            

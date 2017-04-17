class Solution1(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 3
        if n == 2:
            return 8
        a = [0 for i in range(n+1)]
        a[0], a[1], a[2] = 1, 2, 4
        m = 1000000007
        for i in range(3, n+1):
            a[i] = (a[i-1] + a[i-2] + a[i-3]) % m
        for i in range(n):
            a[n] = (a[i] * a[n-1-i] + a[n]) % m
        return a[n]
        
class Solution2(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        M = [[1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0]]
        
        def mul(a, b):
            ans = [[0 for j in range(len(b[0]))] for i in range(len(a))]
            for i in range(len(a)):
                for j in range(len(b[0])):
                    for k in range(len(a[0])):
                        ans[i][j] = (ans[i][j] + a[i][k] * b[k][j]) % 1000000007
            return ans
            
        A = M
        f = [[1], [1], [0], [1], [0], [0]]
        n -= 1
        while n > 0:
            if n % 2 == 1:
                f = mul(A, f)
            A = mul(A, A)
            n /= 2
        ans = 0
        for i in f:
            ans += i[0]
        return ans % 1000000007
    

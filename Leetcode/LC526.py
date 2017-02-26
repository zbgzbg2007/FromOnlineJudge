class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        x = list()
        x.append(list())
        for i in range(N):
            i += 1
            x.append(list())
            for k in range(N):
                k += 1
                if k % i == 0 or i % k == 0:
                    x[i].append(k)
                
        b = [False for i in range(N+1)]
        return self.dfs(x, b, 1, N)
    def dfs(self, x, b, i, N):
        if i == N:
            for j in x[i]:
                if b[j] == False:
                    return 1
            return 0
        ans = 0
        for j in x[i]:
            if b[j] == False:
                b[j] = True
                ans += self.dfs(x, b, i+1, N)
                b[j] = False
        return ans
            

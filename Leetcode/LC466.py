class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        repeat, cnt = [], []
        j, n, m = 0, len(s1), len(s2)
        for k in range(n1):
            for i in range(n):
                if s1[i] == s2[j]:
                    if j == m-1:
                        repeat.append(i)
                        cnt.append(k)
                    j += 1
                    if j == m:
                        j = 0
                        
            for x in range(len(repeat)-1):
                if repeat[x] == repeat[-1]:
                    before = x+1
                    middle = (n1-cnt[x]-1) / (cnt[-1]-cnt[x]) * (len(repeat)-x-1)
                    after = 0
                    c = cnt[x] + (cnt[-1]-cnt[x]) * ((n1-cnt[x]) / (cnt[-1]-cnt[x]))
                    while x < len(repeat)-1 and c+cnt[x+1]-cnt[x] < n1:
                        x += 1
                        after += 1
                        c += cnt[x]-cnt[x-1]
                    return (before+middle+after) / n2
        
        return len(repeat) / n2
                        

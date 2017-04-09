class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = list(str(n))
        i = len(d) - 1
        while i > 0:
            if d[i] <= d[i-1]:
                i -= 1
            else:
                break
        if i == 0:
            return -1
        j = i
        i -= 1
        while j < len(d) and d[j] > d[i]:
            j += 1
        j -= 1
        d[i], d[j] = d[j], d[i]
        i += 1
        e = d[i:]
        e.sort()
        d[i:] = e
        ans = int("".join(d))
        if ans > 2**31-1:
            return -1
        return ans

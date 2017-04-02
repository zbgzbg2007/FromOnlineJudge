class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        myset = dict()
        for i in range(n):
            myset[i] = set([i])
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1 and i != j and min(myset[i]) != min(myset[j]):
                        myset[j] = myset[i] | myset[j]
                        temp = list(myset[j])
                        for x in temp:
                            myset[x] = myset[j]
        sets = set()
        print myset
        for i in range(n):
            if min(myset[i]) not in sets:
                sets.add(min(myset[i]))
        return len(sets)

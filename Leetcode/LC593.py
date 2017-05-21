class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def d(p1, p2):
            return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
        c = collections.Counter()
        l = [p1, p2, p3, p4]
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                c[d(l[i], l[j])] += 1
        return len(c) == 2 and 2 in c.values() and 4 in c.values()

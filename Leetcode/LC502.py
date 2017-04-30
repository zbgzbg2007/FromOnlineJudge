import heapq
class Solution1(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        heap1 = []
        heap2 = []
        n = len(Profits)
        for i in range(n):
            if Capital[i] <= W:
                heapq.heappush(heap1, -Profits[i])
            else:
                heapq.heappush(heap2, (Capital[i], Profits[i]))
        for i in range(k):
            if len(heap1) > 0:
                W -= heapq.heappop(heap1)
            else:
                return W
            while len(heap2) > 0 and heap2[0][0] <= W:
                x = heapq.heappop(heap2)
                heapq.heappush(heap1, -x[1])
        return W
        

class Solution2(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        n = len(Profits)
        a = sorted(zip(Profits, Capital), key=lambda x: x[1], reverse=True)
        possible = []
        for i in range(k):
            while a and a[-1][1] <= W:
                heapq.heappush(possible, -a.pop()[0])
            if possible:
                W -= heapq.heappop(possible)
            else:
                return W
        return W

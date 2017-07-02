class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        pq = []
        a, b = 10**5, -10**5
        for i in range(n):
            a, b = min(a, nums[i][0]), max(b, nums[i][0])
            heapq.heappush(pq, (nums[i][0], i))
        ids = [1]*n
        s, t = a, b
        while True:
            x, i = heapq.heappop(pq)
            if ids[i] >= len(nums[i]):
                break
            if b == x: return [x, x]
            x = nums[i][ids[i]]
            ids[i] += 1
            heapq.heappush(pq, (x, i))
            a, b = pq[0][0], max(b, x)
            if b-a < t-s:
                s, t = a, b
        return [s, t]
        

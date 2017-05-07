import bisect
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if len(nums) == 0:
            return []
        if k == 1:
            return map(float, nums)
        ans = []
        window = []
        flag = k % 2 == 1
        for i in range(len(nums)):
            bisect.insort(window, nums[i])
            if i >= k-1:
                if flag:
                    ans.append(float(window[k/2]))
                else:
                    ans.append((window[k/2] + window[k/2-1])/2.0)
                window.remove(nums[i-k+1])
            
        return ans
            
import heapq
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        heap1, heap2 = [], [] #min heap for larger numbers, max heap for smaller numbers
        cur = dict()
        small, large = 0, 0
        ans = []
        for i, x in enumerate(nums):
            if i >= k:
                y = nums[i-k]
                cur.setdefault(y, 0)
                cur[y] += 1
                if y >= heap1[0]:
                    large -= 1
                else:
                    small -= 1
                while heap1 and cur.get(heap1[0], 0) > 0:
                    cur[heap1[0]] -= 1
                    heapq.heappop(heap1)
                    
                while heap2 and cur.get(-heap2[0], 0) > 0:
                    cur[-heap2[0]] -= 1
                    heapq.heappop(heap2)
            heapq.heappush(heap1, x)
            y = heapq.heappop(heap1)
            while heap1 and cur.get(heap1[0], 0) > 0:
                cur[heap1[0]] -= 1
                heapq.heappop(heap1)
            heapq.heappush(heap2, -y)
            small += 1
            if small > k/2:
                heapq.heappush(heap1, -heapq.heappop(heap2))
                while heap2 and cur.get(-heap2[0], 0) > 0:
                    cur[-heap2[0]] -= 1
                    heapq.heappop(heap2)
                large += 1
                small -= 1

            if i >= k-1:
                if k % 2 == 0:
                    m = (heap1[0] - heap2[0]) / 2.
                else:
                    m = float(heap1[0])
                ans.append(m)
            
        return ans
            

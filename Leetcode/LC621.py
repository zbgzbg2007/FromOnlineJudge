
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c = collections.Counter(tasks).values()
        m = max(c)
        num = c.count(m)
        return max(len(tasks), (m-1)*(n+1)+num)

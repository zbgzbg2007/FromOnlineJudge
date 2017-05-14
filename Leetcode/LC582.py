class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        d = [kill]
        ans = []
        child = dict()
        n = len(pid)
        for i in range(n):
            child.setdefault(ppid[i], [])
            child[ppid[i]].append(pid[i])
        while d:
            x = d.pop()
            if x in child:
                d += child[x]
            ans.append(x)
        return ans

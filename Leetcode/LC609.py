class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for x in paths:
            w = x.split()
            for i in range(1, len(w)):
                f = w[i].split('(')
                name = w[0]+'/'+f[0]
                content = f[1][:-1]
                if content not in d:
                    d[content] = []
                d[content].append(name)
        ans = []
        for x in d:
            if len(d[x]) > 1:
                ans.append(d[x])
                
        return ans
                
        

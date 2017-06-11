class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        n = len(s)
        x = [0]*n
        for i in range(n):
            l = 0
            for w in dict:
                if s.startswith(w, i):
                    l = max(l, len(w))
            x[i:l+i] = [True]*l
        ans = ''
        flag = False
        for i in range(n):
            if True == x[i] and False == flag:
                ans += '<b>' + s[i]
                flag = True
            elif False == x[i] and True == flag:
                ans += '</b>' + s[i]
                flag = False
            else:
                ans += s[i]
        if True == flag:
            ans += '</b>'
        return ans
                
            

class Solution1(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n/2+1):
            if n % i == 0:
                for j in range(i, n, i): 
                    flag = False
                    for k in range(0, i): 
                        if s[j+k] != s[k]:
                            flag = True
                            break 
                    if flag:
                        break
                if flag == False:
                    return True
        return False
        
class Solution2(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s+s)[1:-1]

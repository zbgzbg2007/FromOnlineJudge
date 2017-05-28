class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []: return ''
        ans = ''
        flag = False
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if len(strs[j]) <= i or strs[j][i] != strs[0][i]:
                    flag = True
                    break
            if flag:
                return ans
            ans += strs[0][i]
        return ans

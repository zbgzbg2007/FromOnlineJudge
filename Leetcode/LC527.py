class Solution(object):
    def wordsAbbreviation(self, dic):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        index = dict()
        ans = []
        for i, s in enumerate(dic):
            if len(s) < 4:
                ans.append(s)
            else:
                ab = s[0]+str(len(s)-2)+s[-1]
                ans.append(ab)
                if ab in index:
                    index[ab].append(i)
                else:
                    index[ab] = [i]
        
        for k in index:
            if len(index[k]) != 1:
                l = 1
                words = index[k]
                while len(words) > 1:
                    l += 1
                    mydict = dict()
                    for i in words:
                        ab = dic[i][0:l]+str(len(dic[i])-l-1)+dic[i][-1]
                        if len(ab) >= len(dic[i]):
                            ab = dic[i]
                        if ab not in mydict:
                            mydict[ab] = [i]
                        else:
                            mydict[ab].append(i)
                    words = []
                    for x in mydict:
                        if len(mydict[x]) == 1:
                            ans[mydict[x][0]] = x
                        else:
                            words = words + mydict[x]
        return ans

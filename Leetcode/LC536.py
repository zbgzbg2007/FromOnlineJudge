# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        i = 0
        if s == '':
            return None
        n = len(s)
        while i < n:
            if s[i] != '(':
                i += 1
            else:
                break
        root = TreeNode(int(s[0:i]))
        if i == n:
            return root
        s1 = i
        i += 1
        left, right = 1, 0
        while i < n:
            if left == right:
                break
            if s[i] == '(':
                left += 1
            if s[i] == ')':
                right += 1
            i += 1
        s2 = i
        root.left = self.str2tree(s[s1+1:s2-1])
        if i == n:
            return root
        root.right = self.str2tree(s[s2+1:-1])
        return root

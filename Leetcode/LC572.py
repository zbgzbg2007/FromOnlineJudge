# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not (s and t):
            return s is t
        if s.val == t.val:
            if self.check(s, t):
                return True
        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True
        return False
    def check(self, s, t):
        if not (s and t):
            return s is t
        if s.val != t.val:
            return False
        return self.check(s.left, t.left) and self.check(s.right, t.right)
        
class Solution2(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def convert(s):
            return '$' + str(s.val) + '&' + convert(s.left) + '|' + convert(s.right) + '$' if s else '*'
        return convert(t) in convert(s)

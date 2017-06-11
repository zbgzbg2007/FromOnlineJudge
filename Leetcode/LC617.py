# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        t = TreeNode(0)
        if t1 is not None:
            t.val += t1.val
            l1 = t1.left
            r1 = t1.right
        else:
            l1, r1 = None, None
        if t2 is not None:
            t.val += t2.val
            l2 = t2.left
            r2 = t2.right
        else:
            l2, r2 = None, None
        t.left = self.mergeTrees(l1, l2)
        t.right = self.mergeTrees(r1, r2)
        return t
        

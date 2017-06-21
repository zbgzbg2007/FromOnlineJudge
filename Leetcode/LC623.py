# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            r = TreeNode(v)
            r.left = root
            return r
        self.f(root, v, d-1)
        return root
    def f(self, root, v, d):
        if root is None: return
        if d == 1:
            l = root.left
            r = root.right
            root.left = TreeNode(v)
            root.right = TreeNode(v)
            root.left.left = l
            root.right.right = r
            return 
        self.f(root.left, v, d-1)
        self.f(root.right, v, d-1)

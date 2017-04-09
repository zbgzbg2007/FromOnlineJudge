# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        a = self.f(root)
        return max(a[2], a[0]+a[1]+1)
        
    def f(self, root):
        if root is None:
            return (0, 0, 0) # longest consecutive path <= root, longest consecutive path >= root, longest path without root
        a = self.f(root.left)
        b = self.f(root.right)
        path = max(a[2], a[0]+a[1]+1, b[2], b[0]+b[1]+1)
        l, r = 0, 0
        if root.left is not None:
            if root.val == root.left.val+1:
                l = max(l, 1+a[0])
            if root.val == root.left.val-1:
                r = max(r, 1+a[1])
        if root.right is not None:
            if root.val == root.right.val+1:
                l = max(l, 1+b[0])
            if root.val == root.right.val-1:
                r = max(r, 1+b[1])
        return (l, r, path)
        
        

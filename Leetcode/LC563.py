# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        x = self.f(root)
        return x[0]
        
    def f(self, root):
        # return tuple (tilt of the root, sum of the whole tree)
        if root is None:
            return (0, 0)
        x = self.f(root.left)
        y = self.f(root.right)
        t = x[0]+y[0]+abs(x[1]-y[1])
        s = root.val+x[1]+y[1]
        return (t, s)

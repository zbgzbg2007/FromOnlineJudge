# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        a, ans = self.f(root)
        ans = max(a-1, ans)
        return ans
    
    def f(self, root):
        # return (max distance, max diameter)
        if root is None:
            return (0, 0)
        a, b = self.f(root.left)
        c, d = self.f(root.right)
        y = max(b, d)
        if a + c > b and a + c > d:
            y = a + c
        x = max(a, c) + 1

        return (x, y)
        

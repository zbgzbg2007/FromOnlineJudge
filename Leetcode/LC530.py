# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = set()
        self.search(root, l)
        l = sorted(list(l))
        
        n = len(l)
        ans = abs(l[0] - l[1])
        for i, k in enumerate(l):
            j = i + 1
            if j < n:
                ans = min(ans, abs(l[i] - l[j]))
        return ans
        
    def search(self, root, l):
        if root is None:
            return
        l.add(root.val)
        self.search(root.left, l)
        self.search(root.right, l)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return list()
        lefts, rights, leaves = [root.val], [root.val], list()
        if root.left is not None:
            self.findleft(root.left, lefts)
        self.findleaf(root, leaves)
        if root.right is not None:
            self.findright(root.right, rights)
        rights = rights[::-1]
        if lefts[-1] == leaves[0]:
            del lefts[-1]
        if leaves[-1] == rights[0]:
            del rights[0]
        if lefts and rights and rights[-1] == lefts[0]:
            del rights[-1]
        ans = lefts + leaves + rights
            
        return ans
        
    def findleft(self, root, lefts):
        if root is None:
            return
        lefts.append(root.val)
        if root.left is not None:
            self.findleft(root.left, lefts)
        else:
            self.findleft(root.right, lefts)
    
    def findright(self, root, rights):
        if root is None:
            return
        rights.append(root.val)
        if root.right is not None:
            self.findright(root.right, rights)
        else:
            self.findright(root.left, rights)
            
    def findleaf(self, root, leaves):        
        if root is None:
            return
        if root.left is None and root.right is None:
            leaves.append(root.val)
        self.findleaf(root.left, leaves)
        self.findleaf(root.right, leaves)

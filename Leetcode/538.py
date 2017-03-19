# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        mylist = list()
        self.collect(root, mylist)
        nums = sorted(mylist)[::-1]
        sums = dict()
        i, n = 0, len(mylist)
        while i < n:
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            if len(sums) == 0:
                sums[nums[i]] = nums[i] * (j-i)
            else:
                sums[nums[i]] = sums[nums[i-1]] + nums[i] * (j-i)
            i = j
        self.replace(root, sums)
        return root
            
        
    def replace(self, root, sums):
        if root is None:
            return
        root.val = sums[root.val]
        self.replace(root.left, sums)
        self.replace(root.right, sums)
        
    def collect(self, root, mylist):
        if root is None:
            return 
        mylist.append(root.val)
        self.collect(root.left, mylist)
        self.collect(root.right, mylist)
        

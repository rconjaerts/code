# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        l = []
        curr_level = [root]
        
        while curr_level:
            l.append([x.val for x in curr_level])
            next_level = []
            for x in curr_level:
                if x.left:
                    next_level.append(x.left)
                if x.right:
                    next_level.append(x.right)
            curr_level = next_level if next_level else None
        return l
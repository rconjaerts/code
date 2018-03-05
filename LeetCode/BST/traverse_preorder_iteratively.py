# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        else:
            l = []
            q = [root]
            while q:
                curr = q.pop(0)
                l.append(curr.val)
                
                if curr.left and curr.right:
                    q.insert(0, curr.left)
                    q.insert(1, curr.right)
                elif curr.left:
                    q.insert(0, curr.left)
                elif curr.right:
                    q.insert(0, curr.right)
            return l
                
                
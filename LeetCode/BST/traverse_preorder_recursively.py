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
        elif root.left and root.right:
            curr = [root.val]
            curr.extend(self.preorderTraversal(root.left))
            curr.extend(self.preorderTraversal(root.right))
            return curr
        elif root.left:
            curr = [root.val]
            curr.extend(self.preorderTraversal(root.left))
            return curr
        elif root.right:
            curr = [root.val]
            curr.extend(self.preorderTraversal(root.right))
            return curr
        else:
            return [root.val]
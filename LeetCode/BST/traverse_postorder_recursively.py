# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        if root.left and root.right:
            left_tree = self.postorderTraversal(root.left)
            right_tree = self.postorderTraversal(root.right)
            left_tree.extend(right_tree)
            left_tree.append(root.val)
            return left_tree
        elif root.left:
            left_tree = self.postorderTraversal(root.left)
            left_tree.append(root.val)
            return left_tree
        elif root.right:
            right_tree = self.postorderTraversal(root.right)
            right_tree.append(root.val)
            return right_tree
        else:
            return [root.val]
            
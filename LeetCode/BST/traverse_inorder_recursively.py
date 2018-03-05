# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        elif root.left and root.right:
            left_tree = self.inorderTraversal(root.left)
            right_tree = self.inorderTraversal(root.right)
            left_tree.append(root.val)
            left_tree.extend(right_tree)
            return left_tree
        elif root.left:
            left_tree = self.inorderTraversal(root.left)
            left_tree.append(root.val)
            return left_tree
        elif root.right:
            curr = [root.val]
            right_tree = self.inorderTraversal(root.right)
            curr.extend(right_tree)
            return curr
        else:
            return [root.val]
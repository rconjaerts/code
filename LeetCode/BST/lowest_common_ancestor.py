# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return False
        
        if root.left and root.right:
            left_tree = self.lowestCommonAncestor(root.left, p, q)
            right_tree = self.lowestCommonAncestor(root.right, p, q)
            if type(left_tree) == int:
                return left_tree
            if type(right_tree) == int:
                return right_tree
            
            if (left_tree and right_tree) or ((root == p or root == q) and (left_tree or right_tree)):
                return root.val
            elif left_tree or right_tree or (root == q or root == p):
                return True
            else:
                return False
        elif root.left:
            left_tree = self.lowestCommonAncestor(root.left, p, q)
            if type(left_tree) == int:
                return left_tree
            elif left_tree and (root == q or root == p):
                return root.val
            elif left_tree or (root == q or root == p):
                return True
            else:
                return False
        elif root.right:
            right_tree = self.lowestCommonAncestor(root.right, p, q)
            if type(right_tree) == int:
                return right_tree
            elif right_tree and (root == q or root == p):
                return root.val
            elif right_tree or (root == q or root == p):
                return True
            else:
                return False
        elif root == p or root == q:
            return True
        else:
            return False
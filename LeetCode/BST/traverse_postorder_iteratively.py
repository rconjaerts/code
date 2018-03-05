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

        st1 = [root]
        st2 = []
        
        while st1:
            curr = st1.pop()
            st2.append(curr.val)
            if curr.left:
                st1.append(curr.left)
            if curr.right:
                st1.append(curr.right)
        
        st2.reverse()
        return st2
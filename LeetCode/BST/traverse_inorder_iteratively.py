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

        l = []
        curr = root
        st = []
        
        while curr:
            st.append(curr)
            curr = curr.left
        
        while st:
            curr = st.pop()
            l.append(curr.val)
            curr = curr.right
            while curr:
                st.append(curr)
                curr = curr.left
        return l
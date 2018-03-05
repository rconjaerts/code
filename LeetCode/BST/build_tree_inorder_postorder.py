# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:        
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        # postorder can always indicate to us what the root is of a (sub)-tree, and inorder can help us decide what left, right children are
        if not postorder:
            return []
        
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        else:        
            root_val = postorder[-1]
            root = TreeNode(root_val)
            i = inorder.index(root_val)
            
            # check if there is a left, right or both subtrees
            if not i == 0 and not i == len(inorder)-1:
                root.left = self.buildTree(inorder[:i], [x for x in postorder if x in inorder[:i]])
                root.right = self.buildTree(inorder[i+1:], [x for x in postorder if x in inorder[i+1:]])
            elif i == 0:
                root.right = self.buildTree(inorder[i+1:], [x for x in postorder if x in inorder[i+1:]])
            else:
                root.left = self.buildTree(inorder[:i], postorder[:-1])
        
            return root
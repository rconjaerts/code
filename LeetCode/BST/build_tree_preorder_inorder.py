# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # preorder can always indicate to us what the root is of a (sub)-tree, and inorder can help us decide what left, right children are
        if not preorder:
            return []
        
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        else:        
            root_val = preorder[0]
            root = TreeNode(root_val)
            i = inorder.index(root_val)
            
            # check if there is a left, right or both subtrees
            if not i == 0 and not i == len(inorder)-1:
                root.left = self.buildTree([x for x in preorder if x in inorder[:i]], inorder[:i])
                root.right = self.buildTree([x for x in preorder if x in inorder[i+1:]], inorder[i+1:])
            elif i == 0:
                root.right = self.buildTree(preorder[1:], inorder[i+1:])
            else:
                root.left = self.buildTree([x for x in preorder if not x == inorder[i]], inorder[:i])
        
            return root
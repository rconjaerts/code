# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # function to test if the values in two lists are equal
    def check_list_equality(self, l1, l2):
        if not len(l1) == len(l2):
            return False
        
        for i in range(0, len(l1)):
            if ((not l1[i] and l2[i]) or (l1[i] and not l2[i])) or (l1[i] and l2[i] and not l1[i].val == l2[i].val):
                return False
        return True
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        curr_level = [root]
        while curr_level:
            next_level_left = []
            for x in curr_level:
                next_level_left.append(x.left if x.left else None)
                next_level_left.append(x.right if x.right else None)

            curr_level.reverse()
            next_level_right = []
            for x in curr_level:
                next_level_right.append(x.right if x.right else None)
                next_level_right.append(x.left if x.left else None)
            
            # if there is only None values the tree is symmetric
            # else if the content of both arrays are the same then that level is symmetric
            # else none of these are the case, than a level is not symmetric and we return False
            if all(x is None for x in next_level_left):
                return True
            elif self.check_list_equality(next_level_left, next_level_right):
                curr_level = [x for x in next_level_left if x is not None]
            else:
                return False
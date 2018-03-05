# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        
        curr_level = [root]
        while curr_level:
            next_level = []
            for i in range(0, len(curr_level)):
                if curr_level[i].left:
                    next_level.append(curr_level[i].left)
                if curr_level[i].right:
                    next_level.append(curr_level[i].right)
                if i <= len(curr_level)-2:
                    curr_level[i].next = curr_level[i+1]
            curr_level = next_level
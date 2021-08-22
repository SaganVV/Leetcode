# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = [(root,1)]
        lev_or = []
        while queue:
            node, depth = queue.pop(0)
            if len(lev_or)!=depth:
                lev_or.append([node])
            else:
                lev_or[depth-1].append(node)
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
            

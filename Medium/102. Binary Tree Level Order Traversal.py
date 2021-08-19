# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        depth = 0
        if root:
            queue = [(root, 0)]
            while queue:
                top, depth = queue.pop(0)
                
                if len(ans)>depth:
                    ans[depth].append(top.val)
                else:
                    ans.append([top.val])
                    
                if top.left:
                    queue.append((top.left, depth+1))
                if top.right:
                    queue.append((top.right, depth+1))
                
        return ans

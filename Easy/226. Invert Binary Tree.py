# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        # tree = TreeNode(root.val)
        # tree.left = self.invertTree(root.right)
        # tree.right = self.invertTree(root.left)
        tree = TreeNode()
        stack = [root]
        tree_stack = [tree]
        while stack and tree_stack:
            #print([tree.val for tree in stack])
            stack_top = stack.pop(0)
            tree_top = tree_stack.pop(0)
            tree_top.val = stack_top.val
           
            if stack_top.right:
               # print(stack_top.right.val)
                tree_top.left = TreeNode()
                tree_stack.append(tree_top.left)
                stack.append(stack_top.right)
                
            if stack_top.left:
               # print(stack_top.val)
                tree_top.right = TreeNode()
                tree_stack.append(tree_top.right)
                stack.append(stack_top.left)

        return tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        tree = TreeNode()
        if not root1:
            return root2
        if not root2:
            return root1
        queue_tree1 = [root1]
        queue_tree2 = [root2]
        queue_tree = [tree]
    #    i = 0 
        while queue_tree1 and queue_tree2:
           # i+=1
           # #print(i)
            top1 = queue_tree1.pop(0)
            top2 = queue_tree2.pop(0)
            top = queue_tree.pop(0)
       #     print(top2.val)
            top.val = top1.val+top2.val
            if top1.left:
                if not top2.left:
                    queue_tree2.append(TreeNode())
                else:
                    queue_tree2.append(top2.left)
                queue_tree1.append(top1.left)
                top.left = TreeNode()
                queue_tree.append(top.left)
            elif top2.left:
                queue_tree1.append(TreeNode())
                queue_tree2.append(top2.left)
                top.left = TreeNode()
                queue_tree.append(top.left)
            
            if top1.right:
                if not top2.right:
                    queue_tree2.append(TreeNode())
                else:
                    queue_tree2.append(top2.right)
                queue_tree1.append(top1.right)
                top.right = TreeNode()
                queue_tree.append(top.right)
            elif top2.right:
                queue_tree1.append(TreeNode())
                queue_tree2.append(top2.right)
                top.right = TreeNode()
                queue_tree.append(top.right)
        return tree
# Use level order traversal. If node is None and there is a similar node in other tree, i just create empty TreeNode and add them to stack.
#Time complexity: O(max(m, n)) -  where m and n is count of nodes at the trees.
#Space complexity: O(m+n)

# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            self.inorder_helper(root, res)
        return res
        
    def inorder_helper(self, node, res):
        if node.left:
            self.inorder_helper(node.left, res)
        res.append(node.val)
        if node.right:
            self.inorder_helper(node.right, res)


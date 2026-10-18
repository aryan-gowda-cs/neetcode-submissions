# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(node):
            if node is None:
                return 0
            nonlocal res
            left = dfs(node.left)
            right = dfs(node.right)
            
            node_val = max(node.val, node.val + left, node.val + right)
            res = max(node_val, res, left + right + node.val)
            return node_val
        dfs(root)
        return res
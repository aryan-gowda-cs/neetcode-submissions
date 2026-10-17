# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True
        def dfs(root):
            nonlocal flag
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if max(l,r) - min(l,r) > 1:
                flag = False
            return 1 + max(l,r)
        dfs(root)
        if not flag:
            return False
        else:
            return True
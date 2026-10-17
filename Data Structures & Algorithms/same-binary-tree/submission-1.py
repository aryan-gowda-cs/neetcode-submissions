# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag = True
        def dfs(t1, t2):
            nonlocal flag
            if t1 is None and t2 is None:
                return
            elif t1 is None or t2 is None:
                flag = False
                return
            elif t1.val != t2.val:
                flag = False
                return
            
            dfs(t1.left, t2.left)
            dfs(t1.right, t2.right)
        dfs(p,q)
        return flag 
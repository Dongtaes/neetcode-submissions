# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.dfs(root,res,k)
        return res[k-1]

    
    def dfs(self, root, res, k):
        if not root or len(res) == k:
            return
        
        self.dfs(root.left, res, k)
        res.append(root.val)
        self.dfs(root.right, res, k+1)
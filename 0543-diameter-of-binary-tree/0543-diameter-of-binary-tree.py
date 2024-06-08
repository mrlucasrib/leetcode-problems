# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxPath = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.DFS(root)
        return self.maxPath
    
    def DFS(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
    
        left = self.DFS(root.left)
        right = self.DFS(root.right)
        self.maxPath = max(left+right, self.maxPath)
        return max(left, right) + 1
        
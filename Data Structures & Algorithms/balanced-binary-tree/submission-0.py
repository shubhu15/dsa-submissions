# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return -1, True
            
            hleft, isleftbal = dfs(node.left)
            if not isleftbal:
                return -1, False
            hright, isrightbal = dfs(node.right)
            if not isrightbal:
                return -1, False
            if abs(hleft-hright)>1:
                return -1,False
            
            return max(hleft,hright)+1, True

        h, bal = dfs(root)
        return bal
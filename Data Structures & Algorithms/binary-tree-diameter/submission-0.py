# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return -1,0
            
            dleft, hleft = dfs(node.left)
            dright, hright = dfs(node.right)

            currh = max(hleft, hright)+1

            currd = max(dleft, dright, hleft+ hright)
            return currd, currh

        d,h = dfs(root)
        return d
        
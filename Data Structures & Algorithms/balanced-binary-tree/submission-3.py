# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            is_balanced = left_height[0] and right_height[0] and (abs(left_height[1] - right_height[1]) <= 1)
            height = 1 + max(left_height[1], right_height[1])

            return [is_balanced, height]
        return dfs(root)[0]
    
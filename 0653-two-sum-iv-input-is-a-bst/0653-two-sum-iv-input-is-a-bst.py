# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        save = []
        def dfs(root, k):
            if not root:
                return False

            if k - root.val in save:
                return True

            save.append(root.val)
            
            return dfs(root.left, k) or dfs(root.right, k)
            
        return dfs(root, k)
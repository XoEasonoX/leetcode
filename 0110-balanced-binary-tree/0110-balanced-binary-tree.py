# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return (max(left, right) + 1)
        
    """
    def isBalanced(self, root):
        
        :type root: Optional[TreeNode]
        :rtype: bool
        
        if root is None:
            return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        return(
        self.isBalanced (root.left) and
        self.isBalanced (root.right)
        )
    """
    def isBalanced(self, root):
        return self.maxDepth(root) != -1
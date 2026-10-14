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
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        if self.maxDepth(root.right) - self.maxDepth(root.left) > 1 or self.maxDepth(root.left) - self.maxDepth(root.right) > 1 :
            return False
        return(
        self.isBalanced (root.left) and
        self.isBalanced (root.right)
        )
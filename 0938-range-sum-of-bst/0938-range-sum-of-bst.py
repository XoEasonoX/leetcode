# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):

        def isSum(root):
            if root is None:
                return 0

            left_sum = isSum(root.left)
            right_sum = isSum(root.right)

            current = root.val if low <= root.val <= high else 0

            return current + left_sum + right_sum

        return isSum(root)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):

        def isSum(root, low, high):
            if root is None:
                return 0

            left_sum = isSum(root.left, low, high)
            right_sum = isSum(root.right, low, high)

            current = root.val if low <= root.val <= high else 0

            return current + left_sum + right_sum

        return isSum(root, low, high)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        path = ''
        result =[]
        def findPath(root, path):
            if root is None:
                return

            path = path + ("->" if path else "") + str(root.val)

             # 1. 判斷是否抵達葉節點
            if root.left is None and root.right is None:
                result.append(path)
                return

            # 2. 繼續探索左子樹
            findPath(root.left, path)

             # 3. 繼續探索右子樹
            findPath(root.right, path)
        findPath(root, path)
        return result
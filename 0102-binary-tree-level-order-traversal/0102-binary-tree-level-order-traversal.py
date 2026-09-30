# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans = []
        q = []
        
        if root is None:
            return []
   
        q.append(root)
        
        while q:
            level_size = len(q)
            level = []         
            for _ in range(level_size):
                cur = q.pop(0)
                level.append(cur.val)
                        
                if cur.left:
                    q.append(cur.left)
        
                if cur.right:
                    q.append(cur.right)
            ans.append(level)
        return ans
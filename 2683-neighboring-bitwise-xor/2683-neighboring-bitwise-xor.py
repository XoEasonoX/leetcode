class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        ans = 0
        for x in derived:
            ans ^= x
        return ans == 0
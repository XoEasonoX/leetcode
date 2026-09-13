# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        mid = (r+l) // 2
        while l < r:
            if isBadVersion(mid) == False:
                l = mid + 1
            elif isBadVersion(mid) == True:
                r = mid
            mid = (r+l) // 2
        return mid
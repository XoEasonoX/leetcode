class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        l = 0
        r = x
        while l <= r:
            mid = (l + r) // 2
            if  mid*mid > x:
                r = mid - 1
            elif mid*mid < x:
                l = mid + 1
            else:
                return mid
        return r
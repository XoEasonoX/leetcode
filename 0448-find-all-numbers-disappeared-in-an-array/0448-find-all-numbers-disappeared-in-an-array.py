class Solution(object):
    def findDisappearedNumbers(self, nums):
        l = []
        n = set(nums)
        for m in range(1, len(nums)+1):
            if m not in n:
                l.append(m)
        return l
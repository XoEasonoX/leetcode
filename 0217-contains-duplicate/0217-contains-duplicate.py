class Solution(object):
    def containsDuplicate(self, nums):
        n2 = set(nums)
        return not len(n2) == len(nums)     
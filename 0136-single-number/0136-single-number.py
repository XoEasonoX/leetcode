class Solution(object):
    def singleNumber(self, nums):
        n1 = sum(nums)
        n2 = sum(set(nums))
        return  (n2 * 2 - n1)
            
        
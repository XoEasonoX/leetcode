class Solution(object):
    def missingNumber(self, nums):
        k = ((len(nums) + 1) * (len(nums))) // 2
        for i in range(len(nums)):
            k -= nums[i]  
        return k
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = min(nums)
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return []
        else: 
            ttl = 0
            for i in range (len(nums)):
                ttl += nums[i]
                if ttl <= nums[i]:
                    ttl = nums[i]
                cur = max(cur, ttl)
            return cur 
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        mid=(r+l) // 2
        while l <= r:
            if nums[mid] < target:
                l = mid + 1
                mid = (l+r)//2
            elif nums[mid]>target:
                r = mid-1
                mid= (l+r)//2
            else :
                return mid
        return -1
        
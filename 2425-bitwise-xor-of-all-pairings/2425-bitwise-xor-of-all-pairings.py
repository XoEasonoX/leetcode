class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        a = 0
        if len(nums2) % 2 != 0:
            for c in nums1:
                a ^= c
        if len(nums1) % 2 != 0:
            for c in nums2:
                a ^= c
        return a
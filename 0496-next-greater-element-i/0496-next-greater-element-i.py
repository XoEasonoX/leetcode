class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greater = {}

        for c in nums2 : 
            # not stack or c <= stack[-1]
            while stack and c > stack[-1]: 
                prev = stack.pop()
                next_greater[prev] = c
            stack.append(c)
        
        for c in stack:
            next_greater[c] = -1
        
        return [ next_greater[c] for c in nums1 ]
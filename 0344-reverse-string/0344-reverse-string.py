class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while right > left:
            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1 
            
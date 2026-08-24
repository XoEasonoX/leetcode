class Solution(object):
    def isPalindrome(self, s):
        a = ""
        for x in s:
            if x.isalnum():
                a += x.lower()
        return a[::-1] == a        
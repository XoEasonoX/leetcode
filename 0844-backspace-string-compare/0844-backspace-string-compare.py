class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = []
        t1 = []

        for c in s:
            if c == "#" and s1 :
                s1.pop()

            elif c != "#":
                s1.append(c)

        for c in t:
            if c == "#" and t1:
                t1.pop()

            elif c != "#":
                t1.append(c)
 
        return t1 == s1 
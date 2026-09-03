class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        k = 0
        dic = set(list(jewels))
        for char in stones:
            if char in dic:
                k += 1
        return k        
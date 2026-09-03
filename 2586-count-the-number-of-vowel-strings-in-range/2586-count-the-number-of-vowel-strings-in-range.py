class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        k = 0
        vowel = {'a', 'e', 'i', 'o', 'u'}
        for i in range(left, right + 1):
            char = words[i]
            if char[0] in vowel and char[-1] in vowel:
                k += 1
        return k
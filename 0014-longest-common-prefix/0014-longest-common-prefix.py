class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        result = ""
        first_str = strs[0]
        for i in range(len(first_str)):
            current_char = first_str[i]

            for s in strs:
                if i >= len(s) or s[i] != current_char:
                    return result
            result += current_char
        return result
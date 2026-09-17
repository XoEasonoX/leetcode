class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        g = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in g :
                g[key] = [] 
            g[key].append(s)
        return (g.values())
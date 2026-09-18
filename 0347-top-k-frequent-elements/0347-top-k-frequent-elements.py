class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        g = {}
        r = []
        for s in nums:
            if s not in g:
                g[s] = 0
            g[s] += 1
        g = sorted(g.items(), key= lambda x: x[1], reverse=True)
        g = g[0:k] 
        for l in g:
            r.append (l[0])
        return r
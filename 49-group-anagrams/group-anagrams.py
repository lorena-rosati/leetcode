class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for s in strs:
            ss = ''.join(sorted(s))
            d[ss].append(s)
        
        return d.values()
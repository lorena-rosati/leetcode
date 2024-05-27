class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashMap = {}
        for a in arr:
            hashMap[a] = 1 + hashMap.get(a, 0)
        
        vals = []
        for b in hashMap.values():
            if b in vals:
                return False
            vals.append(b)
        
        return True
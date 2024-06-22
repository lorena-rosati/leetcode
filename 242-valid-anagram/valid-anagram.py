class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False
        
        hashmap = {}
        for l in s:
            hashmap[l] = 1 + hashmap.get(l, 0)
        
        for l in t:
            hashmap[l] = hashmap.get(l, 0) -1
        
        for key in hashmap:
            if hashmap[key] != 0:
                return False
        
        return True
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False

        hashmap = defaultdict(int)

        for c in s:
            hashmap[c] += 1

        for c in t:
            hashmap[c] -= 1

        for key in hashmap:
            if hashmap[key] != 0:
                return False

        return True
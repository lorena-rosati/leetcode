class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if (len(s) != len(t)):
            return False
        else:
            l = list(s)
            for c in t:
                if c in l:
                    l.pop(l.index(c))
                else:
                    return False

        return len(l) == 0


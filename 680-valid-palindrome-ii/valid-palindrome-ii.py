class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1 
        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                s1 = s[:l] + s[l+1:]
                s2 = s[:r] + s[r+1:]
                return s1 == s1[::-1] or s2 == s2[::-1]
        return True
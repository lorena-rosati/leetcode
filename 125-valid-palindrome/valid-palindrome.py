class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            if not self.isAlphaNum(s[l]):
                l += 1
                continue
            if not self.isAlphaNum(s[r]):
                r -= 1
                continue
            if s[r].lower() == s[l].lower():
                l, r = l + 1, r - 1
            else:
                return False
        return True

    def isAlphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") 
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9"))
        
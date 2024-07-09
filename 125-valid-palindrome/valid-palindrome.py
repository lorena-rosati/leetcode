class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            while not self.isAlphaNum(s[l]) and l < r:
                l += 1
            while not self.isAlphaNum(s[r]) and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True
            

    def isAlphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") 
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9"))
        
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strs = ""
        for c in s:
            if self.isAlphaNum(c):
                strs += c.lower()

        return strs == strs[::-1]

    def isAlphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") 
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9"))
        
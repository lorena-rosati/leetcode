class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            if self.isPal(word):
                return word
        return ""         

    def isAlphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9"))

    def isPal(self, word):
        l, r = 0, len(word) - 1
        while l < r:
            while not self.isAlphaNum(word[l]) and l < r:
                l += 1
            while not self.isAlphaNum(word[r]) and l < r:
                r -= 1
            if word[l] != word[r]:
                return False
            l, r = l + 1, r - 1
        return True
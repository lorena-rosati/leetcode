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

    def isPal(self, word):
        l, r = 0, len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            l, r = l + 1, r - 1
        return True
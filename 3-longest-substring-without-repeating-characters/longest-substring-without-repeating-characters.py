class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        l = 0
        hashtable = {} #key is character, value is index

        for r in range(len(s)):
            # if current (end) is already in table, and part of our current substring
            # start substring right after repeat of current character
            if s[r] in hashtable and hashtable[s[r]] >= l:
                l = hashtable[s[r]] + 1
            curr_length = r - l + 1
            max_length = max(curr_length, max_length)
            hashtable[s[r]] = r
        return max_length
            


        
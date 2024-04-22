class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        start = 0
        hashtable = {}
        s_len = len(s)

        for end in range(s_len):
            if s[end] in hashtable and hashtable[s[end]] >= start:
                start = hashtable[s[end]] + 1
            curr_len = end - start + 1
            if curr_len > max_len:
                max_len = curr_len
            hashtable[s[end]] = end
        return max_len


        
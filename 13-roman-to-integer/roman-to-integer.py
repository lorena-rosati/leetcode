class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I': 1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        excep = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

        sum = 0

        for i in range(len(s)):
            if i < len(s)-1 and s[i] in ['I','X','C']:
                # s[keys.index(s[i])+1] == s[i+1] or s[keys.index(s[i])+2] == s[i+1]:
                if s[i:i+2] in excep:
                    sum -= dict[s[i]]
                else:
                    sum += dict[s[i]]
            else:
                sum += dict[s[i]]

        return sum

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        l, r, i = 0, 0, 0

        # while r < len(chars)
        # increment r till next character and increment count
        # write character to i, if count > 1 write count to i + 1
        # move l to r
        while r < len(chars):
            count = 1
            while r + 1 < len(chars) and chars[r] == chars[r + 1]:
                r, count = r + 1, count + 1

            chars[i] = chars[l]
            i += 1

            if count > 1:
                for c in str(count):
                    chars[i] = c
                    i += 1

            r += 1
            l = r

        return i
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            temp = x
            rev = ""
            while temp != 0:
                rev += str(temp % 10)
                temp = temp // 10
            if str(x) == rev:
                return True
            else:
                return False
            
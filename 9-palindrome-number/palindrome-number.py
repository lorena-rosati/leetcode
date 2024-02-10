class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        else:
            temp = x
            rev = 0
            while temp != 0:
                rev = rev*10 + temp%10
                temp = temp // 10
            if x == rev:
                return True
            else:
                return False
            
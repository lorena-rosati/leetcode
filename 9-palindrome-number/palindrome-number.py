class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return self.helper(str(x))

    def helper(self,x):
        if len(x) == 1:
            return True
        elif (len(x) == 2):
            return True if x[0] == x[1] else False
        elif x[0] == x[-1]:
            return self.helper(x[1:len(x)-1]) and True
        else:
            return False
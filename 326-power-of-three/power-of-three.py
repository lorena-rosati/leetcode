class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        elif n==1:
            return True
        elif n%3 != 0:
            return False
        else:
            return self.isPowerOfThree(n/3)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}
        for n in nums:
            if hashmap.get(n, 0) == 1:
                return True
            hashmap[n] = 1
        return False
        
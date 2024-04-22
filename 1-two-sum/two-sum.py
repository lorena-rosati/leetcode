class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = {}
        l = len(nums)
        for i in range(l):
            current = nums[i]
            if (target - current) in hashtable:
                return [hashtable[target-current], i]
            hashtable[current] = i
        return []
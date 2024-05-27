class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = {}
        for i in range(len(nums)):
            if target - nums[i] in hashtable:
                return [hashtable[target - nums[i]], i]
            hashtable[nums[i]] = i
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        ans = [1] * l
        prefix = 1
        for i in range(l):
            ans[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(l-1, -1, -1):
            ans[i] *= postfix 
            postfix *= nums[i]
        
        return ans
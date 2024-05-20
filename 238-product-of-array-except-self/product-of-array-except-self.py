class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre, post, ans = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            pre[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            post[i] = postfix 
            postfix *= nums[i]
        
        for i in range(len(nums)):
            pre[i] *= post[i]

        return pre
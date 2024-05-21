class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
            
        longest = 1
        nums_set = set(nums)

        for n in nums:
            l = 1
            if (n-1) in nums_set:
                continue
            curr = n
            while (curr + 1) in nums_set:
                l += 1
                curr += 1
            longest = max(longest, l)
        
        return longest
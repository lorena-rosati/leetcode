class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_sorted = sorted(nums)

        i, res = 0, []

        for i in range(len(nums)):
            # check if previous is same as current and continue
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                i += 1
                continue
            l, r = i + 1, len(nums_sorted) - 1
            while l < r:
                sum = nums_sorted[i] + nums_sorted[l] + nums_sorted[r] 
                if sum == 0:
                    res.append([nums_sorted[i], nums_sorted[l], nums_sorted[r]])
                    # increment l and if previous one is same keep incrementing in while loop
                    l += 1
                    while nums_sorted[l] == nums_sorted[l-1] and l < r:
                        l += 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1              

        return res
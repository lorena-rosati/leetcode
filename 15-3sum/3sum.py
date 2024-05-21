class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        n = sorted(nums)

        for i in range(len(n)):
            if i > 0 and n[i] == n[i-1]:
                continue

            l, r = i + 1, len(n) - 1
            while l < r:
                sum = n[l] + n[r] + n[i]
  
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    result.append([n[i], n[l], n[r]])
                    l += 1
                    while n[l] == n[l-1] and l < r:
                        l += 1
        return result

        
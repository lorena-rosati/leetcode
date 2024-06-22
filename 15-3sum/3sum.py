class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        n = sorted(nums)

        for a in range(len(n)):
            if a > 0 and n[a] == n[a-1]:
                continue
            l, r = a + 1, len(n) - 1
            while l < r:
                s = n[a] + n[l] + n[r]
                if s == 0:
                    result.append([n[a], n[l], n[r]])
                    l += 1
                    while n[l] == n[l-1] and l < r:
                        l += 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return result

            


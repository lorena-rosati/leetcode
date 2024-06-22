class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, a = 0, len(height) - 1, 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            a = max(a, area)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return a
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        
        a = [[] for _ in range(len(nums)+1)]
        # index is how many times element shows up, value is an array of the values
        for key in d:
            a[d[key]].append(key)
        
        s = []
        count = 0
        for i in range(len(a) - 1, 0, -1):
            if a[i] != []:
                for j in a[i]:
                    s.append(j)
                    count += 1
                    if count == k:
                        return s
        
        return s

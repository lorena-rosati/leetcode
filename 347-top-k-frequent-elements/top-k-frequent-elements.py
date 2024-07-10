class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr = [[] for _ in range(len(nums) + 1)]
        res = []

        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        for key in hashmap:
            arr[hashmap[key]].append(key)

        count = 0
        for i in range(len(nums), 0, -1):
            if arr[i] == []:
                continue
            for j in arr[i]:
                res.append(j)
                count += 1
                if count == k:
                    return res
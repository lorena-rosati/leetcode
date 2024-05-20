class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # have an array of size len(nums) + 1, where each index will have the numbers that occur the index # of times
        # hash map with keys as values and values as # occurences
        hashMap = {}
        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)

        arr = [[] for _ in range(len(nums)+1)]

        for key in hashMap:
            arr[hashMap[key]].append(key)

        result = []
        for i in range(len(arr)-1, 0, -1):
            for n in arr[i]:
                result.append(n)
                if len(result) == k:
                    return result
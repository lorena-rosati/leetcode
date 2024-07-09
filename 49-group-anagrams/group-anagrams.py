class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # default dict of list values
        # keys of dictionary are tuples of the letters in the string
        # values are lists of anagrams for that combination of letters
        # sorted_tuple = tuple(sorted(s))

        hashmap = defaultdict(list)

        for s in strs:
            hashmap[tuple(sorted(s))].append(s)

        return hashmap.values()

        #RUNTIME AND MEMORY COMPLEXITY
        # runtime -> O(n) + O(nlgn) + O(n) = O(nlgn)  ... for loop + sorting + convert to tuple
        # space complexity -> 


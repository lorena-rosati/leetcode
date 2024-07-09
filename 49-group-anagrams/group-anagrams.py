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

        for s in strs: # runtime -> len(strs)
            key = [0] * 26
            for c in s: # runtime -> len(s)
                key[ord(c) - ord('a')] += 1
            hashmap[tuple(key)].append(s)

        return hashmap.values()

#above code
        #runtime -> O(len(strs)*avg len of str in strs)
        #space complexity -> # types of anagrams  *  avg # of variations of each anagram
            # theres also space for each key, but its length of 26 so O(1)

#old
        #RUNTIME AND MEMORY COMPLEXITY
        # runtime -> O(n) + O(nlgn) + O(n) = O(nlgn)  ... for loop + sorting + convert to tuple
        # space complexity -> 


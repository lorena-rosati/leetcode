class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(magazine) < len(ransomNote):
            return False

        hashtable = {}
        for c in magazine:
            hashtable[c] = 1 + hashtable.get(c, 0)
        
        for c in ransomNote:
            hashtable[c] = hashtable.get(c, 0) - 1
            if hashtable[c] < 0:
                return False
        
        return True

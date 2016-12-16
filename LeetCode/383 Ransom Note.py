#  Given an arbitrary ransom note string and another string containing letters from all the
# magazines, write a function that will return true if the ransom note can be constructed from the
# magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        n, m = len(ransomNote), len(magazine)
        if n > m:
            return False
        elif n == m:
            return True if ransomNote == magazine else False
        else:
            for c in ransomNote:
                if c not in magazine:
                    return False
                else:
                    pos = magazine.index(c)
                    magazine = magazine[:pos] + magazine[pos + 1:]

            return True


    def canConstruct(self, ransomNote, magazine):
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
import re

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)


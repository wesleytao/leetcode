class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = (s+s)[1:-1]
        
        return ss.find(s) != -1
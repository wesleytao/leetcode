class Solution(object):
    
    def reverse(self, str, start, end):
        while start < end:
            str[start], str[end] = str[end], str[start]
            end -= 1
            start += 1
    
    
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        self.reverse(str, 0, len(str)-1)
        start = 0
        for i, s in enumerate(str):
            if s ==" ":
                self.reverse(str, start, i-1)
                start = i+1
        self.reverse(str, start, len(str)-1)
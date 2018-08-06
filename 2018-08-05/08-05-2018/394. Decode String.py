class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        nums = ""
        
        stack.append(["", 1])
        for char in s:
            if char.isdigit():
                nums += char
            elif char == "[":
                stack.append(["", int(nums)])
                nums = ""
            elif char == "]":
                st,n = stack.pop()
                stack[-1][0] += st*n
            else:
                stack[-1][0] += char
        return stack[0][0]
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.rank = []
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.rank.append(x)
        self.rank.sort()


    def pop(self):
        """
        :rtype: void
        """
        pop_val = self.stack.pop()
        self.rank.remove(pop_val)
        self.rank.sort()



    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.rank[0]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

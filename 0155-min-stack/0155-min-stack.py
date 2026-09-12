class MinStack(object):

    def __init__(self):
        self.sta = []
        self.ms = []
    
    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.sta.append(value)
        if self.ms == []:
            self.ms.append(value)
        elif self.sta[-1] >= self.ms[-1]:
            self.ms.append(self.ms[-1])
        else:
            self.ms.append(self.sta[-1])

    def pop(self):
        """
        :rtype: None
        """
        self.sta.pop()
        self.ms.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.sta[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.ms[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
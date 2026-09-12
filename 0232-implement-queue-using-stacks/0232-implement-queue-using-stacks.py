class MyQueue(object):

    def __init__(self):
        self.que = []
        self.outque = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.que.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.outque ==[]:
            while self.que:
                self.outque.append(self.que.pop())
        return self.outque.pop()
    
    def peek(self):
        """
        :rtype: int
        """
        if self.outque ==[]:
            while self.que:
                self.outque.append(self.que.pop())
        return self.outque[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return self.que == [] and self.outque == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
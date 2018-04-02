import Queue

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = Queue.LifoQueue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.put(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.get()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        top = self.q.get()
        self.q.put(top)
        return top
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q.empty()
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
print obj.top()
print obj.empty()
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

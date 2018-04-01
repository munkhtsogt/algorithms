class MinStack(object):

    def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stack = []
		
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        m = self.getMin()
        if m > x or m == None:
        	m = x
        self.stack.append((x, m))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        	

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
        	return self.stack[-1][0]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
        	return None
        return self.stack[-1][1]
        


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print minStack.getMin()
minStack.pop()
print minStack.top() 
print minStack.getMin()


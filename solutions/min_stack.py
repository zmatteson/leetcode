"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack:

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
        if not self.stack:
            self.stack.append((x, x))
            return
        else:
            if self.stack[-1][1] >= x:
                self.stack.append((x,x))
            else:
                self.stack.append((x,self.stack[-1][1]))

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            raise IndexError('Stack is empty')
        return self.stack.pop()[0]
        

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            raise IndexError('Stack is empty')
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            raise IndexError('Stack is empty')
        return self.stack[-1][1]    


# Your MinStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MinStack()
    obj.push(10)
    obj.push(1)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
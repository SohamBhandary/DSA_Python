class Stack(list):
    def isEmpty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.isEmpty():
            return super().pop() 
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.isEmpty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self)
    
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
print(s.size())
s.pop()
print(s.peek())
print(s.size())

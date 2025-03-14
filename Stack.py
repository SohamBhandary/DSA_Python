class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0
    
    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self.items)
    
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
s.pop()
print(s.peek())
print(s.size())


        
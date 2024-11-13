class stack:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return len(self.items)==0
    
    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        if not self.is_empty():
           return self.items.pop()
        else:
            raise IndexError("stack is empty")
        
    def peek(self):
        if not self.is_empty():
           return self.items[-1]
        else:
            raise IndexError("stack is empty")

    def size(self):
        return len( self.items)
    
    def print_stack(self):
        
        if not self.is_empty():
            for item in self.items[::-1]:  
                print(item)
        else:
            print("Stack is empty")
   
      
    
s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print("top element is: ",s1.peek())
print("pop element is",s1.pop())
print("top element is: ",s1.peek())
print(s1.print_stack())

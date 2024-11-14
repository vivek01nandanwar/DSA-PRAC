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

'''class Stack:
    def __init__(self, capacity):
        self.capacity = capacity  
        self.stack = [None] * capacity  # Initialize the stack with None values
        self.top = -1  # Top of the stack (empty stack means top is -1)
    
    def is_empty(self):
        return self.top == -1 
    
    def is_full(self):
        return self.top == self.capacity - 1  
    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack Overflow")
        self.top += 1  # Move the top pointer
        self.stack[self.top] = item  
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")  
        item = self.stack[self.top]  
        self.top -= 1  # Move the top pointer down
        return item  # Return the popped item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")  
        return self.stack[self.top]  # Return the item at the top of the stack
    
    def size(self):
        return self.top + 1 

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements from top to bottom:")
            for i in range(self.top, -1, -1):  
                print(self.stack[i])

# Example usage
stack = Stack(5)  # Create a stack of size 5
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print("Stack elements:")
stack.print_stack()

print("Top element:", stack.peek())  # Should print 50
print("Popped element:", stack.pop())  # Should print 50

stack.print_stack()  # Should print the stack after popping an element
'''
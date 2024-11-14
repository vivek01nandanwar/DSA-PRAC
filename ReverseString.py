class Stack:
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
    
def revstring(st):
    stack=Stack()
    for stri in st:
        stack.push(stri)

    revst=""
    while not stack.is_empty():
        revst+=stack.pop()
    return revst

input_string = "Hello, World!"
print("Original string:", input_string)
print("Reversed string:", revstring(input_string))

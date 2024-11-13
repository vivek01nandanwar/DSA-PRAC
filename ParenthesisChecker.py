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

    def size(self):
        return len( self.items)
    
    def print_stack(self):
        
        if not self.is_empty():
            for item in self.items[::-1]:  
                print(item)
        else:
            print("Stack is empty")
   
      
def MatchingOp_close(exp):
    stack=Stack()
    parenthesisPair={'(':')','[':']','{':'}'}
    for expression in exp:
        if expression in '([{':
            stack.push()
        elif expression in '}])':
            if stack.is_empty or stack.pop()!=parenthesisPair[expression]:
                return False
    return stack.is_empty()
    
expression_1 = "{[()()]}"
expression_2 = "{[(])}"
expression_3 = "({[({})]})"
expression_4 = "((())"

print(f"Expression: {expression_1} is balanced: {MatchingOp_close(expression_1)}")
print(f"Expression: {expression_2} is balanced: {MatchingOp_close(expression_2)}")
print(f"Expression: {expression_3} is balanced: {MatchingOp_close(expression_3)}")
print(f"Expression: {expression_4} is balanced: {MatchingOp_close(expression_4)}")


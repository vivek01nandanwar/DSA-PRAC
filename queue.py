class Queue:
    def __init__(self):
        self.items=[]
        # self.front=None
        # self.rear=None
    def is_empty(self):
        return len(self.items)==0
    
    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("queue underflow")
    
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("queue underflow")
    
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("queue underflow")
    
    def size(self):
        return len(self.items)
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("front=",q1.get_front()," rear=",q1.get_rear())
try:
    q1.dequeue()
    print("queue has now",q1.size(),"elements")
except IndexError as e:
    Exception(e.args[0])

print("front=",q1.get_front()," rear=",q1.get_rear())
 
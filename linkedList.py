import time




class LinkedElement:
    def __init__(self, val):
        self.next = None
        self.value = val
    
class Queue:
    def __init__(self):
        self.last = None
        self.first = None
        self.size = 0
    
    def enqueue(self, value):
        item = LinkedElement(value)
        if(self.first == None):
            self.last = item
            self.first = item
        else:
            self.last.next = item
            self.last = item
    
    def dequeue(self):
        item = self.first.value
        self.first = self.first.next
        return item
    

def main():
    size = 10000000
    q = Queue()
    
    for i in range(size):
        q.enqueue(i)
    
    for i in range(size):
        print(q.dequeue(), end=", ")

    return 0
    
t = time.time()
main()
t1 = time.time()
print(t1 - t)
    
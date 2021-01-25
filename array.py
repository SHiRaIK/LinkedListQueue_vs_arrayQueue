import time

    # QueueScript slow as fuck
class QueueScript:
    def __init__(self):
        self.items = []
    
    def enqueue(self, value):
        self.items.insert(0, value)
    
    def dequeue(self):
        return self.items.pop()

class Queue:
    def __init__(self):
        self.items = []
        self.last = 0
        self.first = 0
    
    def enqueue(self, value):
        self.items.append(value)
        self.last += 1
    
    def dequeue(self):
        #self.resize() # resize slows down and doesnt free memory
        if(self.first == self.last):
            return None
        item = self.items[self.first]
        self.first += 1
        return item

    def resize(self):
        if(self.last - self.first <= self.first and self.first > 100):
            count = 0
            while(self.first < self.last):
                self.items[count] = self.items[self.first]
                count += 1
                self.first += 1
            self.last = self.first
            self.first = 0
            return
        else:
            return

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
#timeit.timeit('main()', number=5)
    
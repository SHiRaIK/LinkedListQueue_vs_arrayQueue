import linkedListQueue
import arrayQueue

def insertLinkedListQueue():
    number = 5000000
	
    lq = linkedListQueue.Queue()
    for i in range(10000000):
        if(i == number):
            continue
        lq.enqueue(i)
    print(linkedListQueue.insert(number, lq))
'''
def insertArrayQueue():
    number = 5000000
	
    aq = arrayQueue.Queue()
    for i in range(10000000):
        if(i == number):
            continue
        aq.enqueue(i)
    print(arrayQueue.insert(number, aq))
'''
def main():
    arrayQueue.enqueueDequeue()
    
    linkedListQueue.enqueueDequeue()
    
    arrayQueue.enqueueTest()
    
    linkedListQueue.enqueueTest()
	
    arrayQueue.dequeueTest()
    
    linkedListQueue.dequeueTest()
	
    insertLinkedListQueue()
	
    insertArrayQueue()
    
    return 0
    
main()














    
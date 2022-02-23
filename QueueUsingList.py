'''
Queue with python list with out the size limit

'''

class Queue():
    def __init__(self):
        self.items = []

    def __str__(self):
        value = [str(x) for x in self.items]
        return " ".join(value)
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self,value):
        self.items.append(value)

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            return self.items[0]
    
    def delete(self):
        self.items = None

cusTomQueue = Queue()
cusTomQueue.enqueue(1)
cusTomQueue.enqueue(2)
cusTomQueue.enqueue(3)
cusTomQueue.dequeue()
print(cusTomQueue)        
class Queue:
    def __init__(self,size):
        self.size = size
        self.front=self.rear = -1
        self.queue = [0]*self.size

    def enqueue(self,data):
        if self.rear == -1:
            self.front=self.rear=0
            self.queue[self.rear]=data
            return
        if self.rear+1 == self.size:
            print("is_full")
            return
        self.rear+=1
        self.queue[self.rear] = data

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("empty")
            return
        for i in range(self.front , self.rear+1):
            print(self.queue[i],end=" ")

    def dequeue(self):
        if self.front ==-1 or self.front>self.rear:
            print("empty")
            return
        self.front+=1

    def front(self):
        if self.front == -1 or self.front > self.rear:
            print("empty")
            return
        print(self.queue[self.front])



obj = Queue(3)
obj.enqueue(18)
obj.enqueue(7)
obj.display()
obj.dequeue()
print()
obj.display()
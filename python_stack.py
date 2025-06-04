class stack:
    def __init__(self):
        self.box = []
        self.box2 = []

    def push(self,data):
        self.box.append(data)

    def display(self):
        if len(self.box)==0:
            print("empty")
            return
        for i in self.box[::-1]:
            print(i,end=" ")

    def pop(self):
        if len(self.box) == 0:
            print("empty")
            return
        self.box.pop()

    def peek(self):
        if len(self.box) == 0:
            print("empty")
            return
        print(self.box[-1])

stack1 = stack()
stack1.push(18)
stack1.push(7)
stack1.display()
stack1.pop()
stack1.pop()
print()
stack1.display()
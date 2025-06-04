class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.prev =  None

class Double_linked_list:
    def __init__(self):
        self.head = self.tail = None

    def b_insert(self,data):
        newnode = Node(data)
        if self.head is None:
            self.tail = self.head = newnode
            return
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    def e_insert(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def forward_display(self):
        if self.head is None:
            print("empty Linked_list")
            return
        cur = self.head
        while cur:
            print(cur.data,end="->")
            cur = cur.next

    def backward_display(self):
        if self.head is None:
            print("empty Linked_list")
            return
        cur = self.tail
        while cur:
            print(cur.data,end="->")
            cur = cur.prev

obj=Double_linked_list()

obj.b_insert(int(input("enter Value to insert: ")))
obj.b_insert(int(input("enter Value to insert: ")))
obj.e_insert(int(input("enter Value to insert: ")))
obj.e_insert(int(input("enter Value to insert: ")))

obj.forward_display()
print()
obj.backward_display()
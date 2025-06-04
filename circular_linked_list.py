class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    def b_insert(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
            return

        cur=self.head
        while cur.next is not self.head:
            cur = cur.next
        newnode.next = self.head
        self.head = newnode
        cur.next = newnode


    def e_insert(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
            return

        cur = self.head
        while cur.next is not self.head:
            cur = cur.next
        newnode.next = self.head
        cur.next = newnode


    def position(self,pos):
        if pos<=0:
            print("invalid position")
            return
        cur = self.head
        for i in range(pos-1):
            if cur.next == None:
                break
            cur = cur.next
        else:
            print(cur.data)
            return cur

    def b_delete(self):
        if self.head is None or self.head.next is self.head:
            self.head = None
            return
        cur = self.head
        while cur.next is not self.head:
            cur = cur.next
        cur.next = self.head.next
        self.head = self.head.next

    def e_delete(self):
        cur = self.head
        while cur.next.next is not self.head:
            cur = cur.next
        cur.next = self.head

    def display(self):
        if self.head is None:
            print("empty")
            return
        cur = self.head
        while cur:
            print(cur.data, end="->")
            if cur.next == self.head:
                break
            cur = cur.next

obj=CircularLinkedList()
obj.b_insert(3)
obj.b_insert(2)
obj.b_insert(1)
obj.e_insert(4)
obj.e_insert(5)
obj.display()
print()
obj.b_delete()
obj.e_delete()
obj.display()
print()
obj.position(2)
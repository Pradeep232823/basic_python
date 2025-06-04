class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head=None

    # To insert in Begin of Linked List
    def b_insert(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    # To insert in End of Linked List
    def e_insert(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newnode

    # To display Linked List
    def display(self):
        if self.head is None:
            print("empty")
            return
        cur = self.head
        while cur:
            print(cur.data,end="->")
            cur = cur.next

    # To delete End number in Linked List
    def e_delete(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next=None

    # To delete Begin number in Linked List
    def b_delete(self):
        if self.head is None:
            return
        self.head = self.head.next

    def position(self,pos):
        if pos<=0:
            print("invalid position")
            return
        cur = self.head
        for i in range(pos-1):
            if cur.next==None:
                break
            cur = cur.next
        else:
            return cur

    # To delete the particular position number
    def pos_delete(self, pos):
        if pos <= 0:
            print("invalid position")
            return
        if pos == 1:
            self.b_delete()
            return
        cur = self.position(pos - 1)
        if cur and cur.next:
            cur.next = cur.next.next
            return
        else:
            print("position not found")
            return

    # To delete middle number in Linked List
    def value_delete(self,data):
        cur = self.head
        while cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
                return
            cur = cur.next

obj = Linked_list()

obj.b_insert(8)
obj.b_insert(10)
obj.b_insert(11)

obj.e_insert(36)
obj.e_insert(3)

obj.display()

print()
print()

# obj.e_delete()
# obj.b_delete()
obj.value_delete(int(input("enter Value to delete: ")))
obj.display()
print()

obj.pos_delete(int(input("enter position to delete: ")))
obj.display()
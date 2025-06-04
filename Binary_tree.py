class Node:
    def __init__(self,data):
        self.data =data
        self.left=None
        self.right=None
class BinaryTree:

    def findnode(self,root,key):
        if root is None:
            return None

        if root.data == key:
            return root
        left = self.findnode(root.left,key)
        if left:
            return left
        return self.findnode(root.right,key)

    def height(self,node):
        if node is None:
            return -1
        return 1+max(self.height(node.left),self.height(node.right))

    def height_of_key(self,key):
        if key is root:
            key = root.data
        node=self.findnode(root,key)
        if node is None:
            return -1
        return self.height(node)

    def depth(self,root,key):
        if key is root:
            return 0
        if root is None:
            return -1
        if root.data==key:
            return 0
        left=self.depth(root.left,key)
        if left !=-1:
            return left+1
        right = self.depth(root.right, key)
        if right!=-1:
            return right+1
        return -1

    def inorder_traversal(self,root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data,end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self,root):
        if root:
            print(root.data, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self,root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data, end=" ")

root = Node(5)
obj=BinaryTree()
root.left = Node(6)
root.right = Node(12)
root.right.right = Node(3)
root.left.left = Node(10)
root.left.right = Node(33)
root.left.left.left=Node(56)
obj.inorder_traversal(root)
print()
obj.preorder_traversal(root)
print()
obj.postorder_traversal(root)
print()
print(obj.height(root)-1)
print(obj.depth(root,root))
print(obj.height_of_key(root))
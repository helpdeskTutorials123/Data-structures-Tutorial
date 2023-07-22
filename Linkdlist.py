# Linked List implementation WITHOUT insert_at_end() FUNCTION

# Activity 01 Implement Node class in python
class Node: 
    def __init__(self, dataval): 
        self.dataval = dataval 
        self.next = None


# Activity 02 Create another LinkedList class using the above Node class.
class LinkedList: 
    def __init__(self): 
        self.head = None 
        
    def insert_at_head(self, dataval): 
        new_node = Node(dataval) 
        new_node.next = self.head 
        self.head= new_node 

    def traverse(self): 
        n = self.head 
        while n is not None: 
            print(n.dataval, end=' ') 
            n = n.next


# Activity 03 implement the function insert_at_end() in the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_head(self, dataval):
        new_node = Node(dataval)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, dataval):
        new_node = Node(dataval)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def traverse(self):
        n = self.head
        while n is not None:
            print(n.dataval, end=' ')
            n = n.next


# Create actual liked list
my_list = LinkedList()
my_list.insert_at_end(1)
my_list.insert_at_end(2)
my_list.insert_at_end(3)
my_list.traverse()  # Output: 1 2 3

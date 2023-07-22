# This function is in LinkedList class.
# Inserts a new node after the given prev_node. This method is
# defined inside LinkedList class shown above */
def insertAfter(self, prev_node, new_data):

	# 1. check if the given prev_node exists
	if prev_node is None:
		print("The given previous node must inLinkedList.")
		return

	# 2. Create new node &
	# 3. Put in the data
	new_node = Node(new_data)

	# 4. Make next of new Node as next of prev_node
	new_node.next = prev_node.next

	# 5. make next of prev_node as new_node
	prev_node.next = new_node

# Data insert into end of a linkdlist

class LinkedList:
    def __init__(self):
        self.head = None
        
    def at_end(self, dataval):
        new_node = Node(dataval)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        


# Create actual liked list
my_list = LinkedList()
my_list.at_end(1)
my_list.at_end(2)
my_list.at_end(3)
my_list.traverse()  # Output: 1 2 3

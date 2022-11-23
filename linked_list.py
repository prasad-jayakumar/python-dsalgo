class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    ## WRITE LL CONSTRUCTOR HERE ##
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
            

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

 
my_linked_list = LinkedList(1)

my_linked_list.append(3)

my_linked_list.print_list()

### Test cases for pop #####
print(my_linked_list.pop())

print(my_linked_list.pop())

print ('\n final list')
my_linked_list.print_list()
print(my_linked_list.pop())

#######################
                                                                                                                    
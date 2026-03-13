class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        if self.head is None:
            self.__init__(value)
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def prepend(self, value):
        pass
    def insert(self, value, position):
        pass
    def pop(self):
        if self.length == 0:            return None
        current = self.head
        previous = self.head
        while current.next is not None:
            previous = current
            current = current.next
        self.tail = previous
        self.tail.next = None
        self.length -= 1

ll = LinkedList(1)
ll.append(2)
ll.print_list()
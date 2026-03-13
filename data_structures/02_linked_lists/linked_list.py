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

    def get(self,index):
        if index < 0 or index >= self.length: return None
        current = self.head
        for _ in range(index):
            current = current.next
        print(current.value)
        return current
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index <0 or index > self.length: return False
        if index == 0: return self.prepend(value)
        if index == self.length: return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index <0 or index >= self.length: return None
        if index == 0: return self.pop_first()
        if index == self.length-1: return self.pop()
        previous = self.get(index-1)
        temp = previous.next
        previous.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

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
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def pop_first(self):
        if self.length == 0: return None
        current = self.head
        self.head = self.head.next
        current.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return True

    def pop(self):
        if self.length == 0: return None
        current = self.head
        previous = self.head
        while current.next is not None:
            previous = current
            current = current.next
        self.tail = previous
        self.tail.next = None
        self.length -= 1
        if self.length ==0:
            self.head = None
            self.tail = None
        return current.value

    def reverse(self):
        if self.length == 0: return 
        if self.length == 1: return self.head.value
        temp = self.head
        self.head = self.tail
        self.tail = temp
        next = temp
        curr = temp.next
        while curr.next is not None:
            prev = curr.next
            curr.next = next
            next = curr
            curr = prev
        
        curr.next = next
        self.tail.next = None

    def reverse_clean(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def middle(self):
        slow = self.head
        fast = self.head
        # fast.next == None or fast None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.value
            
        

ll = LinkedList(1)
ll.append(2)
# ll.print_list()
# ll.pop()
ll.print_list()
ll.append(3)
ll.append(4)
ll.append(5)
ll.print_list()
print("===========", end="\n")
ll.reverse()
print("===========", end="\n")
ll.print_list()
print("===========", end="\n")
print("middle: ", ll.middle())
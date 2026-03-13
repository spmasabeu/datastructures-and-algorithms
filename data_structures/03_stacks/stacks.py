class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height+=1
        return True

    def pop(self):
        if self.height == 0: return False
        if self.height ==1: self.top = None
        top = self.top
        self.top = top.next
        top.next = None
        self.height-=1
        return top
        

stack = Stack(5)
stack.print_stack()
stack.push(1)
stack.push(10)
stack.print_stack()
stack.pop()
stack.print_stack()


print("======================")

class StackList:
    def __init__(self):
        self.stack_list = []

    def push(self,value):
        self.stack_list.append(value)
    
    def pop(self):
        self.stack_list.pop()

    def peek(self):
        if len(self.stack_list) == 0: return None
        return self.stack_list[-1]
    
    def is_empty(self):
        return len(self.stack_list)==0

s = StackList()
print(s.is_empty())
s.push(5)
print(s.stack_list)
print(s.pop())

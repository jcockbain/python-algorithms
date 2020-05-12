from Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def insert_at_head(self, val):
        temp_node = Node(val)
        temp_node.next = self.head_node
        self.head_node = temp_node
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print(temp.val, "-> None")
        return True

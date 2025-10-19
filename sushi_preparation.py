# Nunyie
# BSCpE 2-2
# Sushi Preparation with Linked List

class SushiNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self, data):
        new_node = SushiNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = SushiNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
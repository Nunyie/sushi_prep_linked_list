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

    def insert_at_beginning(self, data):
        new_node = SushiNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = SushiNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_beginning(self):
        if not self.head:
            raise ValueError("Cannot remove from an empty list")
        data = self.head.data
        self.head = self.head.next
        return data

    def remove_at_end(self):
        if not self.head:
            raise ValueError("Cannot remove from an empty list")
        if not self.head.next:
            data = self.head.data
            self.head = None
            return data
        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        return data

    def remove_at(self, data):
        if not self.head:
            return None
        if self.head.data == data:
            return self.remove_beginning()
        current = self.head
        while current.next:
            if current.next.data == data:
                removed_data = current.next.data
                current.next = current.next.next
                return removed_data
            current = current.next
        return None

    def __str__(self):
        if not self.head:
            return ""
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return ", ".join(result)
    
# Sample Code
sushi_preparation = LinkedList()
sushi_preparation.insert_at_end("prepare")
sushi_preparation.insert_at_end("roll")
sushi_preparation.insert_at_beginning("assemble")

# Output
print(sushi_preparation)
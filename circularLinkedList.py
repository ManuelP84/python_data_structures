from node import Node

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, index, data):
        """
        Insert a new element to the Circle Linked List
        """      

        if  self.size == 0 and self.head is None:
            self.head = Node(data, None)
            self.head.next = self.head
            self.size += 1
        else:
            probe = self.head
            while index >0 and probe.next != self.head:
                probe = probe.next
                index -= 1
            probe.next = Node(data, probe.next)
            self.size += 1

    def iter(self):
        """
        Generates an iterator from the Circle Linked List
        """
        
        probe = self.head

        while probe.next != self.head:
            value = probe.data
            probe = probe.next
            yield value
        yield probe.data

    def sizer(self):        
        return self.size
    
    def delete(self, data):
        """
        Delete an element from a Circle Linked List
        """  

        if self.size == 0:
            print("The Circular Linked List is already empty")

        elif self.size == 1:
            if self.head.data == data:
                self.head = None
                self.size = 0
            else:
                print(f"The element: '{data}' is not in the Circular Linked List.")

        elif self.head.data == data:
            probe = self.head
            while probe.next != self.head:
                probe = probe.next
            self.head = self.head.next
            probe.next = self.head
            self.size -= 1

        else:
            probe = self.head
            previous = self.head
            while probe.next != self.head and probe.data != data:
                previous = probe
                probe = probe.next
            
            if probe.data == data:
                previous.next = probe.next
                self.size -=1
            else:
                print(f"The element: '{data}' is not in the Circular Linked List.")
    
    def list_items(self):
        """
        Convert a Circle Linked List into a List
        """

        list_items = []
        for item in self.iter():
            list_items.append(item)

        return list_items
from twoWayNode import TwoWayNode

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def append(self, data):
        # Insert a new twoWayNode at the head of the SinglyLinkedList
        
        if self.head is None:
            self.head = TwoWayNode(data, self.tail, self.head)
            self.tail = self.head
            self.size += 1
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next
            probe.next = TwoWayNode(data, probe, probe.next)
            self.tail = probe.next
            self.size +=1

    def iter(self):
       # Generates an iterator  
        probe = self.head

        while probe:
            value = probe.data
            probe = probe.next
            yield value
    
    def size(self):
        # Return the size of the double linked list
        return self.size

    def clear(self):
        # Clear the double linked list        
        self.head = None
        self.tail = self.head
        self.size = 0

    def delete(self, data):
        #Delete a node in the double linked list
        probe = self.head

        while probe:
            if probe.data == data:
                if probe == self.head:
                    if probe.next != None:
                        self.head = probe.next
                        self.head.previous = None
                        self.size -= 1
                        return probe.data
                    else:
                        self.tail = probe.previous
                        self.head = probe.next
                        self.size -= 1
                        return probe.data                    
                elif probe.next == None:
                    self.tail = probe.previous
                    self.tail.next = None
                    self.size -= 1
                    return probe.data
                else:
                    probe.previous.next = probe.next
                    probe.next.previous = probe.previous
                    self.size -= 1
                    return probe.data
            
            probe = probe.next

        print(f"The element: {data} is not in the Double Linked List")

    def replace(self, target_item, new_item):
        #Replace an certain item in the double linked list
        probe = self.head

        while probe != None and probe.data != target_item:
            probe = probe.next
        
        if probe != None:
            probe.data = new_item
        else:
            print(f'Sorry...Data: "{target_item}" is not in the linked list!')

    def str(self):
        # String format representation of the data of the linked list
        probe = self.head
        items = ""

        while probe:        
            items += str(probe.data) + " "
            probe = probe.next
        print(items)

from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0
    
    def append(self, data):
        # Insert a new node at the head of the SinglyLinkedList
        node = Node(data)
        
        if self.tail == None:
            self.tail = node
            self.size += 1
            #self.head = node
        else: 
            probe = self.tail
            
            while probe.next:
                probe=probe.next
            
            probe.next = node
            #self.head = node
            self.size += 1
     
    def size(self):
        #Return the size of the linked list
        return self.size

    def iter(self):
        #Returns elements from tail to head
        probe = self.tail

        while probe:
            value = probe.data
            probe = probe.next
            yield value
    
    def delete(self, data):
        #Delete a node in the linked list
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    self.head = current.next
                    return current.data
                else:
                    previous.next = current.next
                    self.size -= 1
                    if self.head==current:
                        self.head = previous
                    return current.data
            
            previous = current
            current = current.next

    def removeAtHead(self):
        #Remove the head element in the linked list
        probe = self.tail

        if probe is None:
            print(f'The linked list is already empty')

        elif probe.next is None:
            removed_item = probe.data
            self.tail = None
            self.size -=1
            print(f'The item: {removed_item}. Was succesfully removed')
        
        else:
            while probe.next.next != None:
                probe = probe.next
            removed_item = probe.next.data
            probe.next = None
            self.size -= 1
            #self.head = self.head.next
            print(f'The item: {removed_item}. Was succesfully removed')

    def removeAtTail(self):
        #Remove the head element in the linked list    

        if self.tail == None:
            print(f'The linked list is already empty')

        elif self.tail.next == None:
            removed_item = self.tail.data
            self.tail = None
            self.size -=1
            print(f'Data: "{removed_item}" succesfully removed!')

        else:
            removed_item = self.tail.data
            self.tail = self.tail.next
            self.size -=1
            print(f'Data: "{removed_item}" succesfully removed!')
  
    def search(self, data):
        # Search a node in the linked list. Using iter() method
        found=False
        for node in self.iter():
            if data == node:
                print(f'Data: "{data}" found!')
                found = True
        if found!=True:
            print(f'Sorry...Data: "{data}" NOT found!')    

    def find(self, data):
        # Search a node in the linked list. Using the probe
        probe = self.head
        
        while probe != None and data != probe.data:
            probe = probe.next

        print(probe.data)
        
        if probe!=None:
            print(f'Data: "{data}" found!')
        else:
            print(f'Sorry...Data: "{data}" NOT found!')

    def replace(self, target_item, new_item):
        #Replace an certain item
        probe = self.head

        while probe != None and probe.data != target_item:
            probe = probe.next
        
        if probe != None:
            probe.data = new_item
        else:
            print(f'Sorry...Data: "{target_item}" is not in the linked list!')

    def insert_index(self, index):
        # Insert an item from specific index
        probe = self.tail
        
        if probe == None or index<0:
            probe = Node("",probe)
        else:
            while index<1 or probe != None:
                probe = probe.next
                index -= 1
            probe.next = Node("",probe.next)
    
    def delete_index(self, index):
        # Delete an item from specific index
        probe = self.tail

        if probe == None:   
            print(f'The linked list is already empty')

        elif probe.next == None or index<0:
            removed_item = probe.data
            print(f'Data: "{removed_item}" succesfully removed!')
            probe = probe.next
        
        else:
            while index>0 and probe.next.next !=None:
                probe = probe.next
                index -= 1
            removed_item = probe.next.data
            probe.next = probe.next.next
            print(f'Data: "{removed_item}" succesfully removed!')

    def clear(self):
        # Clear the linked list
        self.tail = None
        self.head = None
        self.size = 0

    def str(self):
        # String format representation of the data of the linked list
        probe = self.tail
        items = ""

        while probe:        
            items += str(probe.data) + " "
            probe = probe.next
        print(items)

    
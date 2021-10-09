
import random

class Array(object):
    def __init__(self, capacity: int, fill_value: int =None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index: int):
        return self.items[index]

    def __setitem__(self, index: int , new_item):
        self.items[index] = new_item
    
    def pushitem(self, new_item):
        self.items.append(new_item)

    def sumitems(self):
        sum = 0
        for index in range(self.items.__len__()):
            sum += self.items[index]           
            #sum = sum + self.__getitem__(i)
        return sum
        
    def randomitems(self, min, max):
        for index in range(self.items.__len__()):
            self.items[index]=random.randint(min,max)            
            #self.__setitem__(index, random.randint(min,max))
from customArray import Array
import random

class Grid:
    def __init__(self, rows: int, columns: int, fill_value: int = None):
        self.data = Array(rows)
        
        for row in range(rows):               
            self.data[row] = Array(columns, fill_value) #Doing so it implements the dunder method __setitem__() of the class Array
    
    def get_height(self):
        return len(self.data) #Doing so it implements the dunder method __len__() of the class Array  
        #self.data.__len__.()            
        
    def get_width(self):
        return len(self.data[0]) #Doing so it implements the dunder method __len__() of the class Array            

    def __getitem__(self, index: int):
        return self.data.__getitem__(index)
        #return self.data[index] #Doing so it implements the dunder method __getitem__() of the class Array
    
    def __str__(self):
        #Str format of the grid
        result = ""
        
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                result += str(self.data[row][column]) + " "
            result += "\n"
        return str(result)

    def randomitems(self, min: int , max: int):  
        #Fill the grid with random numbers      
        for row in range(self.get_height()):
            for column in range (self.get_width()):
                self.data[row][column]=random.randint(min, max)
    
    def sumitems(self):
        # Sum all the items in the grid
        sum = 0
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                sum += sum + self.data[row][column]
        return sum
    
    def max_item(self):
        # Return the max number in the grid
        max = 0
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                if self.data[row][column]>max:
                    max = self.data[row][column]
        return max
    
    def min_item(self):
        # Return the min number in the grid
        min = 0
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                if self.data[row][column]<min:
                    min = self.data[row][column]
        return min
                    

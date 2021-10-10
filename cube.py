import random
from customArray import Array
from customGrid import Grid

class Cube:

    def __init__(self, rows: int, columns: int, depth: int, fill_value: int = None):
        self.data = Grid(rows , columns)
        for row in range(rows):
            for column in range(columns):
                self.data[row][column] = Array(depth, fill_value)

    def get_height(self):
        "Returns the height of the cube"
        return self.data.get_height()
    
    def get_width(self):
        "Returns the width of the cube"
        return self.data.get_width()
    
    def get_depth(self):
        "Returns the depth of the cube"
        return len(self.data[0][0])

    def get_item(self, index: int):
        "Returns an item of the cube"
        return self.data[index]
    
    def set_item(self, row, column, depth, new_item):
        "Sets an item in a certain position of the 3 dimensional array"
        self.data[row][column][depth]= new_item

    def __str__(self):
        "String representation of the 3 dimensional array"
        result=""
        print("\n")
        for deep in range(self.get_depth()):
            for row in range(self.get_height()):
                for column in range(self.get_width()):
                    result += str(self.data[row][column][deep]) + " "
                result += "\n"
            result += f"Grid {deep+1}\n\n"
        return result

    def randomitems(self, min:int, max: int):
        "Sets random items to the 3 dimensional array"
        for deep in range(self.get_depth()):
            for row in range(self.get_height()):
                for column in range(self.get_width()):
                    self.data[row][column][deep]= random.randint(min, max)
            
        

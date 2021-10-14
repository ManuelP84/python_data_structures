
from linkedList import SinglyLinkedList
from customArray import Array

def arrayToList(array: Array) -> SinglyLinkedList:
    """Generate an random array and turned into a Linked list"""
    linkedList = SinglyLinkedList()

    for item in iter(array):
        linkedList.append(item)
    return linkedList


def run():
    array = Array(10) #Crates an Array object
    array.randomitems(0,10) # Fill the array with random int numbers between 0 ans 10
    print(str(array)) # Prints the str format representation of the array
    numbers = arrayToList(array) #Turn the array into a SinglyLinkedList
    numbers.str() # Print the str format representation of the SinglyLinkedList

if __name__=="__main__":
    run()






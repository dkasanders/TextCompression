import sys

#Own implementation of a heap for have the elements be ordered such that each element is greater than or equal to its children
class Heap:
    #If given a list when initializing, order that list
    #If the given variable is an element, create an array with just that element.
    def __init__(self, val):
        if type(val) == list:
            this.array = val
        else:
            this.array = [val]



class Node:
    def __init__(self, character, frequency):
        this.character = character
        this.frequency = frequency



if len(sys.argv) > 1:
    open
    file = open(sys.argv[1], 'r', encoding="utf8")
    lines = file.readlines()
    for line in lines:
        for c in line:
            print(c)

else:
    print("Error: No file given")

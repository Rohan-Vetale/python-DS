'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Program to Reverse the order of items in the array

'''
from array import array
my_array = array('i',[1, 2, 3, 4, 5])
reversed_array = array('i', reversed(my_array))
print("\nReversed Array items:")
for item in reversed_array:
    print(item, end="")
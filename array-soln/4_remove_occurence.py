'''
@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Program to Remove the first occurence of a given element

'''
from array import array
my_array = array('i', [1, 2, 3, 4, 5])
element_to_remove = 2
if element_to_remove in my_array:
    my_array.remove(element_to_remove)
    print(f"\nArray after removing the first occurrence of {element_to_remove}: {my_array}")
else:
    print(f"\nElement {element_to_remove} not found in the array.")
'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Program to count the occurences of an element in array

'''

from array import array
my_array = array('i', [1, 2, 3, 4, 5])
# Get the number of occurrences of a specified element in the array
specified_element = 3
occurrences = my_array.count(specified_element)
print(f"\nThe number of occurrences of {specified_element} in the array: {occurrences}")
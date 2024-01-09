'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Python program to add array of integers and printing them individually

'''
from array import array
# Create an array of 5 integers and display the array items.
my_array = array('i',[1, 2, 3, 4, 5])

# Access individual elements through indexes and display them
print("Array items:")
for i in range(len(my_array)):
    print(f"Index {i}: {my_array[i]}")
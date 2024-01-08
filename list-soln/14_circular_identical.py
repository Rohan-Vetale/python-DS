'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to check whether two lists are circularly identical

'''

# Check if two lists are circularly identical

# Input lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 1, 2, 3]

if len(list1) == len(list2):
    if sorted(list1) == sorted(list2):
        print("Given two lists are circularly identical")
        
else:
    print("The lists are not identical")
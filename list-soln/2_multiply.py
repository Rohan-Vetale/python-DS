'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to print total multiplies of all elements in the list

'''
list2 = [1, 2, 4, 6, 8]
multi = 1
for item in list2:
    multi *= item
    
print(f"Multiplication of all the items in the list is {multi}")
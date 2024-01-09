'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Python program to add member(s) in a set.

'''
my_set = {'carrot', 'banana', 'apple'}
print(f"Original set is {my_set}")
how_many = int(input("How many elements do you want to add in this set?  "))
for _ in range(how_many):
    my_set.add(input("Enter the element you want to add now  "))
    
print(f"Updated set after adding new elements : {my_set}")
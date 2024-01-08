'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to print the difference betweent two lists

'''
list1 = [10, 20, 30, 40]
list2 = [10, 50, 30, 60]
list_diff = set(list2) - set(list1)
print(list_diff)
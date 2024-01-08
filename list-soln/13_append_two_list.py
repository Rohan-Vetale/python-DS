'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to print total multiplies of all elements in the list

'''

list1 = [10, 20, 30, 40]
list2 = [10, 50, 30, 60]
print(f"List before appending is {list1}")
list1.extend(list2)
final_list = set(list1)
print(f"List after appending is {final_list}")
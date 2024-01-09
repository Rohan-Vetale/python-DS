'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Python program to remove item(s) from set

'''
my_set = {'carrot', 'banana', 'apple', 'jackfruit', 'pineapple'}
print(f"Original set is {my_set}")
try:
    item_to_remove = input("Enter the item that you want to remove from this set : ")
    my_set.remove(item_to_remove)
    print(f"Updated set after removing {item_to_remove} is {my_set}")
except:
    print(f"The item {item_to_remove} is not present in the set, please try again")

'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Python program to Remove an item from a tuple

'''

tuple_with_item_to_remove = (1, 2, 3, 4, 5)
item_to_remove = 3
modified_tuple = tuple(item for item in tuple_with_item_to_remove if item != item_to_remove)
print("Tuple after removing the item:", modified_tuple)

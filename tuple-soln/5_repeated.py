'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Python program to Find repeated items of a tuple

'''

tuple_with_duplicates = (1, 2, 3, 2, 4, 5, 3)
repeated_items = [item for item in tuple_with_duplicates if tuple_with_duplicates.count(item) > 1]
print("Repeated items:", repeated_items)

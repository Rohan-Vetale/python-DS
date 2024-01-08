'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to print the common items between two lists

'''

# Find common items from two lists

# Input lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Find common items
common_items = []

# Iterate through elements in list1
for item in list1:
    # Check if the element is in list2
    if item in list2:
        common_items.append(item)

# Output the common items
if common_items:
    print("Common items:", common_items)
else:
    print("No common items found.")

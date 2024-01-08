'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to sort the list by the second element of each tuple

'''
# Sample List
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sort the list of tuples based on the last element
sorted_list = sorted(sample_list, key=lambda x: x[-1])

# Print the result
print("Original List:", sample_list)
print("Sorted List:", sorted_list)

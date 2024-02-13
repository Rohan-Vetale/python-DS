'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Program to Count number of items in a dictionary value that is a list

''' 
sample_dict_with_lists = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6, 7, 8]}
list_items_count = sum(len(value) for value in sample_dict_with_lists.values() if isinstance(value, list))
#isinstance returns true if value is list type
print("Count of items in dictionary values that are lists:", list_items_count)
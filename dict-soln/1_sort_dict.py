'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Sort a dictionary by value (ascending and descending)

''' 
sample_dict = {3: 30, 1: 10, 2: 20}

ascending_sorted_dict = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
descending_sorted_dict = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending Sorted Dictionary:", ascending_sorted_dict)
print("Descending Sorted Dictionary:", descending_sorted_dict)
'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to print unique lists in a list

'''
sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

unique_list = []
for sublist in sample_list:
    if sublist not in unique_list:
        unique_list.append(sublist)

print("Sample List:", sample_list)
print("New List:", unique_list)

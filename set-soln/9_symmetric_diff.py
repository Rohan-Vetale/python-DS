'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title :  Python program to create a symmetric difference

''' 

my_set = {'carrot', 'banana', 'apple'}
your_set = {'carrot', 'banana', 'apple', 'jackfruit', 'pineapple'}
union_set = my_set.union(your_set)
inter_set = my_set.intersection(your_set)
symm_diff_set = my_set.symmetric_difference(your_set)
print(f"Symmetric Difference between {my_set} and {your_set} is {symm_diff_set}")
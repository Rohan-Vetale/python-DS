'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title :  Python program to create set difference.

''' 
my_set = {'carrot', 'banana', 'apple'}
your_set = {'carrot', 'banana', 'apple', 'jackfruit', 'pineapple'}
union_set = my_set.union(your_set)
inter_set = my_set.intersection(your_set)
diff_set = union_set - inter_set
print(f"Difference between {my_set} and {your_set} is {diff_set}")
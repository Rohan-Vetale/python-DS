'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title :  Python program to find maximum and the minimum value in a set

'''  
your_set = {1, 2, 3, 4, 5, 6, 7, 8, 12, 22, 87, 45, 77, 46, 35}
''' Without using inbuilt methods
min_val = 10000
max_val = 0
for item in your_set:
    if item < min_val:
        min_val = item
    elif item > max_val:
        max_val = item
        
print(f"Min val is {min_val}")
print(f"Max val is {max_val}")'''
min_val = min(your_set)
max_val = max(your_set)
print(f"Min val is {min_val}")
print(f"Max val is {max_val}")
'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to print total permutations in the list

'''

from itertools import permutations

#Get an input list defination
input_list = [33, 14, 512, 55, 99]

# Generate parmutations
permutations_list = list(permutations(input_list))

# Display the result
for perm in permutations_list:
    print(perm)


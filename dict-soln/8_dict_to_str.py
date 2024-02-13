'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Program to count char in string and create dict accordingly

''' 
str1 = "w3resource"
my_dict = {}
for char in str1:
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1

print(my_dict)
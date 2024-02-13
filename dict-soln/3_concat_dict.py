'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Program to concatenate dicts to create new dicts

''' 

dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
new_dict = {}
new_dict = dict1 | dict2 | dict3

print(new_dict)
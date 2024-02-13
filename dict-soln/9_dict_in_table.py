'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Program to print dictionary in a table format

''' 
my_dict = {0: 10, 1: 20, 2: 20, 3:30}
print("Dictionary in table format:")
for key, value in my_dict.items():
    print(f"| {key} | {value} |")
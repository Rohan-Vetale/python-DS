'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to lower case the first N characters

'''

input_str = input("Enter the string that you want : ")
num_of_char = int(input("Enter the number of first how many characters you want to lower cased : "))
out_str = input_str[:num_of_char].lower() + input_str[num_of_char:]
print(out_str)
'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to reverse a string without inbuilt function

'''

input_str = input("Enter the string you want to reverse : ")
#reverse the string using string slicing
output_str = input_str[::-1]
print(f"Output string of {input_str} is {output_str}")
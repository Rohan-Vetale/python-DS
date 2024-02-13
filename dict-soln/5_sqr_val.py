'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Program to print a dictionary with key as number and value as number*number

''' 
num_of_times = int(input("Enter the value of N for the dictionary creation : "))
my_dict = {}
for i in range(1,num_of_times+1):
    my_dict[i] = i*i

print(my_dict)
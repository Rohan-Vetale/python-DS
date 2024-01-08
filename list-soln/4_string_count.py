'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to print total number of strings that have starting and ending character same

'''
list4 = ['maximum', 'lol', 'make', 'cake']
counting = 0
for element in list4:
    first_char = element[0]
    if len(element) >= 2 and element.endswith(first_char):
        counting += 1
        
print(counting)

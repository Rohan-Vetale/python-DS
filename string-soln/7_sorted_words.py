'''

@Author: Rohan Vetale

@Date: 2024-01-07 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-07 18:00:30

@Title : Program to print sorted list from a given, comma seperated, user input

'''

words = str(input("Enter the words seperated by a comma and then hit enter : "))
list_of_words = words.split(", ")
print(sorted(list_of_words))
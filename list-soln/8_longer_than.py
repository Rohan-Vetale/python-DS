'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to find the list of words that are longer than n from a given list of words

'''
num_of_words = int(input("How many words do you want in your list? : "))
longer_than = int(input("Enter the longer than number : "))
list_of_words = []
longer_list = []
for i in range(num_of_words):
    word = input(f"Enter the {i}th word : ")
    list_of_words.append(word)

for word in list_of_words:
    if len(word) > longer_than:
        longer_list.append(word)

print(f"From the original list {list_of_words} the words longer than {longer_than} are {longer_list}")
'''

@Author: Rohan Vetale

@Date: 2024-01-07 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-07 18:00:30

@Title : Program to print the length of the longest word from a list of words by user input

'''

#taking user input
num_of_words = int(input("How many words do you want to enter? : "))
list_of_words = []
for i in range(1,num_of_words+1):
    word = input(f"Enter the {i}th word : ")
    list_of_words.append(word)


#Calculating the length of each word in the list 
max_len = 0
for word in list_of_words:
    if len(word) > max_len:
        max_len = len(word)
        
#Printing the length of the word from the list that has maximum length
print(max_len)
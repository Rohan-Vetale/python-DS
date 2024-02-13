'''

@Author: Rohan Vetale

@Date: 2024-01-07 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-07 18:00:30

@Title : Print the frequency of a character in a given string and given format

'''


def count_character_frequency(input_string):
    """
        Description:
        Returns character frequency from a given string

        Parameter:
        input_string : String that needs to be analyzed for each character frequency

        Return:
        char_frequency : Returns character frequency from a given string
    """
    #created a dict to store char as key and freq as their value
    char_frequency = {}
    for char in input_string:
        if char in char_frequency:
            #there exists a key char in dict so just add their value by 1
            char_frequency[char] += 1
        else:
            #the key is not present in the dict so just add it in the dict and then assign the value as 1
            char_frequency[char] = 1
    return char_frequency

# Test the function
input_str = "google.com"
result = count_character_frequency(input_str)
print("Character frequency:", result)

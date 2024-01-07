'''

@Author: Rohan Vetale

@Date: 2024-01-07 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-07 18:00:30

@Title : Get the part before a specified character from a given input string

'''

# Solution 8
def get_last_part_before_character(input_string, specified_char):
    """
        Description:
        Function used to get the part before a specified character

        Parameter:
        input_string : String that needs to be broken down into parts

        Return:
        last_part : Part before the specified character
    """
    last_part = input_string.rsplit(specified_char, 1)[0]
    return last_part

# Test the function
input_str = 'https://www.google.com/search'
specified_character = '/'
result = get_last_part_before_character(input_str, specified_character)
print("Last part before specified character:", result)

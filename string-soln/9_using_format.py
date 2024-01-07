'''

@Author: Rohan Vetale

@Date: 2024-01-07 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-07 18:00:30

@Title : Format the given string in a given format

'''
# Solution 9
def display_formatted_text(input_text):
    """
        Description:
        Function used to display the string in format

        Parameter:
        input_text : String that needs to be formatted

        Return:
        input_text : Formatted text
    """
    formatted_text = '{:^50}'.format(input_text)
    return formatted_text

# Test the function
input_text = "This is a sample text for formatting."
result = display_formatted_text(input_text)
print("Formatted text (width=50):")
print(result)

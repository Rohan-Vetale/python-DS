'''

@Author: Rohan Vetale

@Date: 2024-01-07 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-07 18:00:30

@Title : Program to add ing or ly to a string based on certain conditions

'''

def add_ing(input_str):
    """
        Description:

        Function to add ing or ly to a given input string

        Parameter:

        input_str : String that user has given to add suffixes 'ing' or 'ly'
        
        Return:
        out_str : String containing suffixes 'ing' or 'ly' based on certain conditions
    
    """

    if len(input_str) >= 3:
        if input_str.endswith("ing"):
            out_str = input_str + "ly"
        else:
            out_str = input_str + "ing"
    else:
        out_str = input_str
    return out_str


input_str = "caring"
result = add_ing(input_str=input_str)
print(result)

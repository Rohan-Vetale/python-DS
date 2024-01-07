'''

@Author: Rohan Vetale

@Date: 2024-01-07 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-07 18:00:30

@Title : Replace all the occurences of the first character in a given string with $ except for the first char

'''

def replace_char(input_str):
    """
    Description:

    To replace all char from first char except first char from a given string

    Parameter:

    input_str : String that needs to be replaced for each character frequency

    Return:

    converted_str : Returns replaced string according to the given condition
    
    """
    to_replace = input_str[0]
    replaced_str = [] #list of replaced chars
    replaced_str.append(to_replace)
    for char in range(1,len(input_str)):
        replace_now = input_str[char]
        if replace_now == to_replace:
            replaced_str.append('$')
        else:
            replaced_str.append(replace_now)
    
    converted_str = "".join(replaced_str) #converting the list to string using .join() method
    return converted_str
    
            
    
    
string1 = "google gets the good giggles"
response = replace_char(string1)
print(response)
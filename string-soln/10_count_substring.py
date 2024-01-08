'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to count the occurences of a given substring

'''

def count_substring(input_str, inp_substr):
    """
        Description:
        Function used to count the occurences of a substring inside of a given input string

        Parameter:
        input_str : Actual string given by user
        inp_substr : Substring that needs to be checked inside of the actual string

        Return:
        occurences : Number of times the substring occurs in the given actual string
    """
    occurences = input_str.count(inp_substr)
    return occurences


input_str = input("Enter the actual string : ")
inp_substr = input("Enter the substring to count its occurences inside of actual string : ")
result = count_substring(input_str=input_str, inp_substr=inp_substr)
print(f"The total number of occurences for {inp_substr} is {result}")

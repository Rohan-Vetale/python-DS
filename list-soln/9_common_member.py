'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Python function that takes two lists and returns True if they have at least one common member.

'''
list1 = [2, 4, 6, 8, 10]
list2 = [1, 3, 5, 8, 11]

def common():
    """
        Description:
        Function that takes two lists and returns True if they have at least one common member.

        Parameter:
        None
        
        Return:
        True or False : If they have at least one common member
    """
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                print(f"Found an element that is common between two lists, the number is {element2}")
                return True
            
            
common()      
        

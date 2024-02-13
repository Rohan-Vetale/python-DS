'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Program to print the unique values for a key in dictionary

''' 


sample_data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
               {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

unique_values = set(val for d in sample_data for val in d.values())
print("Unique Values:", unique_values)

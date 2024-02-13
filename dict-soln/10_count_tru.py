'''

@Author: Rohan Vetale

@Date: 2024-01-09 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-09 18:00:30

@Title : Program to count number of true values in the given dictionary

''' 
sample_data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
true_counts = 0
for element in sample_data:
    if element['success'] == True:
        true_counts += 1

print(f"Total true counts are : {true_counts}")

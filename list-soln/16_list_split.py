'''

@Author: Rohan Vetale

@Date: 2024-01-08 09:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-08 18:00:30

@Title : Program to split the list by first char

'''

sample_list = ["apple", "banana", "orange", "avocado", "blueberry", "kiwi", "peach", "grape"]

result_dict = {}
for word in sample_list:
    first_char = word[0].lower()
    if first_char in result_dict:
        result_dict[first_char].append(word)
    else:
        result_dict[first_char] = [word]

print("Sample List:", sample_list)
for key, value in result_dict.items():
    print(f"Words starting with '{key}': {value}")

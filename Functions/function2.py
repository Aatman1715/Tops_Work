#Code to merge more than two dictionaries in Python and print the merged dictionary using a function.
def merge_dictionaries(*dicts):
    merged_dict = {}
    for d in dicts:
        merged_dict.update(d)
    return (merged_dict)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}
merged_dict = merge_dictionaries(dict1, dict2, dict3)
print("Merged Dictionary:", merged_dict)  
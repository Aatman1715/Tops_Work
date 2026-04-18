#Lambda function to add 3 numbers
# add_numbers = lambda a, b, c: a + b + c
# result = add_numbers(5, 10, 15)
# print(result)

#Lambda function to sort the list by the second element
#Make 2 lists 
# list1 = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
# list2 = [(4, 'grape'), (6, 'orange'), (5, 'pear')]
# sorted_list1 = sorted(list1, key=lambda x: x[1])
# sorted_list2 = sorted(list2, key=lambda x: x[1])
# print(sorted_list1)
# print(sorted_list2)

#Lambda function to sort dictionary by values
my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)
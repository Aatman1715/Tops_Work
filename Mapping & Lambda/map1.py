#Convert list of celcuius to farenhit using map function
celsius_list = [0, 20, 37, 100]
farenhit_list = list(map(lambda c: (c * 9/5) + 32), celsius_list)
print(farenhit_list)

#Code to get the following output using map function
#lst_number = [1, 2, 3, 4, 5]
#output = [1, 4, 9, 16, 25]
lst_number = [1, 2, 3, 4, 5]
squared_output = list(map(lambda x: x**2, lst_number))
print(squared_output)

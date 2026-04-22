#Code to understand various methods of arrays in python
#1. Creating an array
import array as arr
#Creating an array of integers
my_array = arr.array('i', [1, 2, 3, 4, 5])
print("Array of integers:", my_array)
#2. Accessing elements of an array
print("First element:", my_array[0])
print("Last element:", my_array[-1])
#3. Modifying elements of an array
my_array[2] = 10
print("Modified array:", my_array)
#4. Appending elements to an array
my_array.append(6)
print("Array after appending:", my_array)
#5. Inserting elements at a specific position
my_array.insert(1, 15)
print("Array after inserting 15 at index 1:", my_array)
#6. Removing elements from an array
my_array.remove(10)
print("Array after removing 10:", my_array)
#7. Popping elements from an array
popped_element = my_array.pop(2)
print("Popped element:", popped_element)
print("Array after popping:", my_array)
#8. Slicing an array
sliced_array = my_array[1:4]
print("Sliced array (index 1 to 3):", sliced_array)
#9. Iterating through an array
print("Iterating through the array:")
for element in my_array:
    print(element)
#10. Finding the length of an array
print("Length of the array:", len(my_array))
#11. Concatenating two arrays
another_array = arr.array('i', [7, 8, 9])
concatenated_array = my_array + another_array
print("Concatenated array:", concatenated_array)
#12. Reversing an array
my_array.reverse()
print("Reversed array:", my_array)
#13. Sorting an array
my_array.sort()
print("Sorted array:", my_array)
#14. Finding the index of an element
index_of_15 = my_array.index(15)
print("Index of 15:", index_of_15)
#15. Counting occurrences of an element
count_of_1 = my_array.count(1)
print("Count of 1 in the array:", count_of_1)
#16. Clearing an array
my_array.clear()
print("Array after clearing:", my_array)
"""
List are ordered sequences and can hold variety of object types, supports indexing and slicing, they can be nested.
Lists are mutable, sort and append doesnt return anything, just a function call and can be used later

"""

list1 = ['one', 'two', 'three']
list2 = ['four', 'five']
my_list = list1 + list2
my_list[0] = 'ONE ALL CAPS'
my_list.append('six')
my_list.pop(0)
print(my_list)

char_list = ['a', 'f', 'r', 'c', 'b']
num_list = [1, 5, 7, 3, 2, 10]
char_list.sort()
num_list.sort()
print(char_list)
print(num_list)

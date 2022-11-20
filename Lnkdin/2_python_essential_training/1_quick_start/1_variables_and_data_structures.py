# Variables

x = 5
print(x)

# Float is a decimal number
print(1.2313)

# Imaginary numbers can be used

print(2j)
print(1j * 1j)

# Strings
print('string 1 ' + 'string 2')
print('1' + '1')

#  You cannot add a string and an interger together I.E. '1' + 1

# Booleans

True 
true = True
1 == 1
1 == 2

# Data Structures

# Lists

my_list = [1,2,3,4]
print(my_list)

my_list = ['list', 'of', 'strings']

my_list = [1, 'list', False, []]

my_list = [[1,2,3], [False,True], []]

len(my_list)

# Sets

my_set = {1,2,3,4,5}
print(my_set)

type(my_set)
len(my_set)

my_set = {1,1,2,2}
print(len(my_set))
print(my_set)

[1,2] == [2,1] # FALSE
{1,2} == {2,1} # TRUE

# Tuples, we cannot add or delete from tuples with my_tuple.append
#   tuples are efficient

my_tuple = (1,2,3)
len(my_tuple) # 3
(1,2) == (2,1) #False

# Dictionary

my_dictionary = {'apple': 'A red fruit', 'bear': 'A scary animal'}
print(my_dictionary['apple'])

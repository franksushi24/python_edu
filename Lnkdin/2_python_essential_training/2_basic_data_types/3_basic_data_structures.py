# LISTS

# LIST SLICING

mylist = [1,2,3,4,5]
mylist[3:]

mylist[0:6:2] #= mylist[::2]
# = 1,3,5

for i in range(100):
    print(i)

mylist = list(range(100))

mylist[::-1]
#this lists the integers backwards, increase the super set to step backwards with bigger leaps

mylist = [1,2,3,4]

mylist.append(5)

mylist.insert(3,'a new value')

mylist.remove('a new value')

mylist.pop()

while len(mylist): #while items in list has items, pop. this is a true false statement. rn its false
    print(mylist.pop)

print(mylist)
# empty

a = [1,2,3,4,5]
b = a.copy
#creates a new varable thats a copy of the list

# Tuples and sets

myset = {'a','b','c'}
myset = set(('a','b','c'))

mylist = ('a','b','b','c','c')
mylist = list(set(mylist))
# = ['a','b','c'] deduplicated
myset.add('d')

'a' in myset
# = True
'z' in myset
# = False

while len(myset):
    print(myset.pop())

myset = {'a','b','c'}
myset.discard(a)

#TUPLES

mytuple = ('a','b','c')
mytuple[0] # = 'a'
#mytuple[0] = 'd' does not work. Tuples dont allow item assignment

def returnsMultipleValues():
    return 1,2,3
type(returnsMultipleValues()) # = Tuple, things automatically become tuples when separated by commas

a,b,c = returnsMultipleValues

print(a) # = 1
print (b)# = 2
print(c) # = 3 This is called unpacking values

#DICTIONARIES 

animals = {
    'a':'aardvark',
    'b':'bear',
    'c':'cat',
    }

animals['a'] # = aardvark
animals['d'] = 'dog'
print(animals)
animals['a'] = 'anetelope'

animals.keys()
animals.values()

list(animals.keys)
animals.get('e','elephant') # = if cant find e returns elephant

animals = {
    'a':['aardvark','antelope'],
    'b':['bear'],
    }
animals['b'].append('bison')
animals['c'] = ['cat']

if 'c' not in animals:
    animals ['c'] = []

animals['c'].append('cat')

from collections import defaultdict

animals = defaultdict(list)

animals['e'].append('elephant')
animals['e'].append('emu')

#LIST COMPREHENSIONS

mylist = [1,2,3,4,5]
[2*item for item in mylist] # SQUARE BRACKETS SURROUND LIST COMPREHENSION
# = [2,4,6,8,10]

#filters

mylist = list(range(100))

filteredlist = [item for item in mylist if item % 10 == 0]
filteredlist
#filteredlist = 0 10 20 30 40 50 60 70 80 90
filteredlist = [item for item in mylist if item % 10 < 3]
filteredlist
# provides all numbers that end in 0 1 or 2

mystring = 'My name is Frankie Abbott. I live in California'
mystring.split('.') #separates strings with period as divider

def cleanword(word):
    return word.replace('.','').lower()

[cleanword(word) for word in mystring.split()]
# = my , name, is, frankie, abbott, i, live, in, california

[cleanword(word) for word in mystring.split() if len(cleanword(word)) < 3]

[[cleanword(word) for word in sentence.split()] for sentence in mystring.split('.')]
# this groups words based on the sentence they are in

#DICTIONARY COMPREHENSIONS

animallist = [('a','aardvark'),('b','bear'),('c','cat'),('d','dog')]
animals = {item[0]: item[1]for item in animallist}
# = {'a':'aardvark','b'...} this created a dictionary from tuples in a list

animals = {key: value for key,value in animallist}
#does the same thing

animals.items()
list(animals.items)
#creates a list from dictionary

[{'letter':key, 'name':value} for key,value in animals.items]
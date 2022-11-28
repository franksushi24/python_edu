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
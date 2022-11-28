#Casting Booleans

bool(1)
bool(-1)
bool(1j)
#True

bool(0)
bool(0j)
#False

# Only a zero integer can be false

bool('True')
# = True

bool('False')
# = True
# Anything but an empty string will be true

bool([])
# = False

bool({})
# = False

mylist = [1,2]
if bool(mylist):
    print('mylist has values in it!')

a = 5
b = 5
if a - b:
    print('a and b are not equal')

a == b
# True or False

# BOOLEAN LOGIC
weatherISnice = False
haveUmbrella = True

if not haveUmbrella or weatherISnice:
    print('stay inside')
else:
    print('go for a walk')

# not haveumbrella is a unit together making the statment false and weather is nice is already false

#STRINGS

#Slicing

name = 'My Name is Frankie Abbott'


name[0]
# = M
name[1]
# = y
name[0:7]
# = My name
name[:7]
# Does the same thing, assumes 0

name[11:]

mylist = [1,2,3,4,5]
mylist[2:4]
# = 3,4

'mynumberis: '+str(5)

f'mynumberis: {5}'

import math

f'pi is: {math.pi:.2f}'
# = 3.14

mystring = '''
Lots of text
lots of text
lots of text
until it ends with \'\'\'
'''

#BYTES

bytes(4)

# to be reviewed later if needed. seems unnecesesarily complicated for really no real reasont to learn
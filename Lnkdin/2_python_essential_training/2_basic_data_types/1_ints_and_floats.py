#INTS AND FLOATS

(20/4)
# = 5.0 not 5

4 + 4.0
# = 8.0

4 * 4.0
# = 16.0

4 ** 4.0
# = 256.0

int(4 ** 4.0)
# = 256

int(8.9)
# = 8

int (14/3)
# = 4

round(14/3)
# = 5

round(14/3, 2)
# = 4.67

1.2 - 1.0
# = 0.19999999999999

# Moral of the story is be careful with floats and integers, funky things can happen

#OTHER TYPES OF NUMBERS

int('100')
# = 100 (this converts string to integer)

int('100', 2)
# = 4 (100 base 2 is 4 from binary)

#from decimal module, import Decimal class and function getcontext
from decimal import Decimal, getcontext

print(getcontext())
# this shows the attributes this function has that can be edited

getcontext().prec=4

Decimal(1)/Decimal(3)
# = 0.3333 with 4 decimal places of precision

Decimal(3.14)
# = 3.1400000000000000000000000000000019489328459814752

Decimal('3.14')
3.14



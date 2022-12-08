#IF ELSE STATEMENTS

for n in range(1,101):
    if n % 15 == 0:
        print("fizzbuzz")
    else:
        if n % 3 == 0:
            print('fizz')
        else:
            if n % 5 == 0:
                print('buzz')
else:
    print(n)

#Elif, accomplishes the same thing but cleaner

for n in range(1,101):
    if n % 15 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
            print('fizz')
    elif n % 5 == 0:
            print('buzz')
    else:
        print(n)

# If else statements do work in a single line of code if formatted correctly as shown below
n = 3
print('fizz' if n % 3 == 0 else n)
fizzbuzz = 'fizz' if n % 3 == 0 else n
'fizz' if n % 3 == 0 else 'buzz' if n % 5 == 0 else n
'fizzbuzz' if n % 15 == 0 else 'fizz' if n % 3 == 0 else 'buzz' if n % 5 == 0 else n
['fizzbuzz' if n % 15 == 0 else 'fizz' if n % 3 == 0 else 'buzz' if n % 5 == 0 else n for n in range (1,101)]  

#WHILE STATEMENTS

from datetime import datetime

datetime.now().second
wait_until = datetime.now().second + 2
while datetime.now().second != wait_until:
    pass

print(f'we are at {wait_until} seconds')

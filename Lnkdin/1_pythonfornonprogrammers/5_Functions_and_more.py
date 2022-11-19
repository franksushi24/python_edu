# FUNCTIONS

def bark():
    print("Woof woof!")
    print("I'm a dog!")

for x in range (100):
    bark()

#       CHALLENGE: Print a function called hello that prints "Hello Nick!"

def hello():
    print("Hello Nick!")

hello()

# PARAMETERS

def hello(name):
    print(f"Hello {name}!")

hello("Frank")

def add_numbers(num1,num2):
    print(num1+num2)

add_numbers(4,8)
add_numbers(3,7)

#       CHALLENGE: Create a function call dog_info that takes in a dog's age and name and prints a sentence about the dog

def dog_info(age,name):
    print(f"{name} is {age} years old and is a great dog!")

dog_info(4,"Spot")

# RETURN

def double(number):
    return number * 2

# print(double(5))
new_number = double(5)

print(new_number)

#       CHALLENGE: Create a function that returns a string in all caps

def uppercase(text):
    return text.upper()

print(uppercase("frank"))

names = ['damie','frank','sara']

for name in names:
    print(uppercase(name))

# INPUT

user_text = input('Enter some text: ')
 
print(user_text.upper())

user_number = input ("What do you want to double? ")

print(int(user_number)*2) # INT TURNS THE USER NUMBER INTO AN INTEGER. OTHERWISE IT WILL DOUBLE THE NUMBER TYPED

#       CHALLENGE: ask for some text, then prompt "Enter 1 to uppercase and 2 to lowercase: " and then either upper or lowercase it.

user_text = input("Enter text here: ")
user_request = input('Enter 1 to uppercase and 2 to lowercase: ')

if user_request is "1":
    print(user_text.upper())
else:
    print(user_text.lower())


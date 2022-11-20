# Classes (introduction to object oriented programming)

class Dog: #This is the object
    def __init__(self, name): #attributes
        self.name = name
        self.legs = 4
    def speak(self): #methods
        print(self.name + ' says: Bark!')

my_dog = Dog('Rover')
another_dog = Dog('Fluffy')

my_dog.speak()
another_dog.speak()
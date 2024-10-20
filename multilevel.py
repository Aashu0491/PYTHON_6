# Base class
class Animal:
    def speak(self):
        print("Animal speaks")

# Intermediate class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Derived class (inherits from Dog)
class Puppy(Dog):
    def play(self):
        print("Puppy plays")


puppy = Puppy()
puppy.speak()  
puppy.bark()   
puppy.play()   

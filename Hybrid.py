# Base class
class Animal:
    def speak(self):
        print("Animal speaks")

# Intermediate class 1 (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Intermediate class 2 (inherits from Animal)
class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Derived class (inherits from Dog and Cat)
class PetDog(Dog, Cat):
    def play(self):
        print("PetDog plays")


petdog = PetDog()
petdog.speak()  
petdog.bark()   
petdog.meow()   
petdog.play()   

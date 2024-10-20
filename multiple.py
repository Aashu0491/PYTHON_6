# Parent Class 1
class Animal:
    def speak(self):
        print("Animal speaks")

# Parent Class 2
class Pet:
    def play(self):
        print("Pet plays")

# Child Class
class Dog(Animal, Pet):
    def bark(self):
        print("Dog barks")


dog = Dog()
dog.speak()  
dog.play()   
dog.bark()   

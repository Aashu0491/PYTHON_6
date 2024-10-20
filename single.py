# Parent Class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()
dog.speak()  
dog.bark()   

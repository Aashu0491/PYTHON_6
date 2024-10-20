# Parent Class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child Class 1
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Child Class 2
class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Create objects of Dog and Cat classes
dog = Dog()
cat = Cat()

dog.speak()  # Inherited from Animal class
dog.bark()   # Defined in Dog class

cat.speak()  # Inherited from Animal class
cat.meow()   # Defined in Cat class

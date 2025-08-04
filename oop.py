#Exercise 1 - Creating a constructor & destructor#
class Person:
  def __init__(self, name, age):    #Constructor
    self.name = name
    self.age = age
  
  def __del__(self):                #Destructor
    self.close()

#Exercise 2 - Magic Methods(str & repr)
class Book:
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
  
  def __str__(self):    #__str__ method
    return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
  
  def __repr__(self):   #__repr__ method
    return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
  
book = Book("Opening Moves","Stephen James", 450)
print(book)

#Exercise 3 - Class Inheritance.
class Animal:
  def __init__(self, eat, sleep):
    self.eat = eat
    self.sleep = sleep
class Dog(Animal):
  def __init__(self, eat, sleep):
    super().__init__(eat, sleep)
  
  def make_sound(self):
    print("barks!")
dog = Dog("Eat", "Sleep")
dog.make_sound()
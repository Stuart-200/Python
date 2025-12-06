class Cat:
    
   def __init__(self,name,age):
        self.name = name
        self.age = age 
        
   def info(self):
        print(f" i am a cat. My name is{self.name}. I am {self.age} years old.")
        
   def make_sound(self):
       print("Meow")
       

class Dog:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
    
    def make_sound(self):
        print("Bark")
        
catone =Cat("jay", 3.4)
dogone = Dog("Tyson", 8)


for animal in (catone, dogone):
    animal.make_sound()
    animal.info()
class Animal:
    def speak(self):
        return 'animal method'
    
class Dog(Animal):
    def speak(self):
        return 'dog method'
    
class Cat(Animal):
    def speak(self):
        return 'cat method'  
    
dog=Dog()
cat=Cat()

print(dog.speak())
print(cat.speak())          
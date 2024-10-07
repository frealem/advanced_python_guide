class Dog:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        return f'{self.name} says woo'
    
dog=Dog('bobby',5)

# print('this is method in in Dog',dog.bark())
    

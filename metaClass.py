class Meta(type):
    
    def __new__(cls,name,bases,attrs):
        attrs['greeting']='hello new class'
        return super().__new__(cls,name,bases,attrs)
    
class My_class(metaclass=Meta):
    pass

print(My_class.greeting) 

# output
# hello new class   
    
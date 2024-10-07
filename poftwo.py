# iteration and loop
# class powerOfTwo:
#     def __init__(self,max=0) :
#        self.max=max
#     def __iter__(self):
#         self.n=0
#         return self
#     def __next__(self):
#         if self.n <= self.max:
#             result=2**self.n
#             self.n +=1
#             return result
#         else:
#             raise StopIteration
    
# print(powerOfTwo.__doc__)
# a=powerOfTwo(4)
# i=iter(a)
# print(i.__next__())
# print(next(i))

# for iteration 

def loop():
    lister=[1,2,3,5,6,7]

    for i in lister:
        print(i,end='=')
        print('hello')
        
loop()        
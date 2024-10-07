"""
Generators
Definition:
Generators are a way to create iterators in Python using the yield statement.
They allow you to iterate over a sequence of values without storing them all in memory at once."""

def countdown(n):
    while n>0:
        yield n
        n-=1
        
for number in countdown(5):
    print('hello',number)        
"""1. Decorators
Definition:
Decorators are a powerful tool in Python that allows you to modify the behavior of functions or methods. They are often used to add functionality to existing code in a clean and readable way.

Key Points:

Decorators are functions that take another function as an argument and extend its behavior without explicitly modifying it.
They are often used for logging, enforcing access control, instrumentation, and caching.
"""

def my_decorator(func):
    
    def wrapper():
        print('this before function is decorated')
        func()
        print('this after the function is decorated')
    return wrapper()
@my_decorator

def added_function():
    print('in between')
    
    
    """ the output:
this before function is decorated
in between
this after the function is decorated
    """
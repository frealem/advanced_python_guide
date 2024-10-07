"""
Definition:
Context managers are a way to manage resources, such as files or network connections,
ensuring that they are properly cleaned up after their use.
The with statement in Python is used to wrap 
the execution of a block with methods defined by a context manager.

"""
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
    

# custom context manager

class MyContext:
    def __enter__(self):
        print("Entering the context.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context.")

with MyContext():
    print("Inside the context.")
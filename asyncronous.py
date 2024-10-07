# asynchronous activities is like this simply
import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)
    print("Goodbye!")

async def main():
    await say_hello()

asyncio.run(main())


# the output will be 
# hello!
# Goodbye!   this is after 1 second
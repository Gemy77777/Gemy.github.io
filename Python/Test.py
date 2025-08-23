def myDecorator(func):
    def wrapper():
        print('#' *50)
        func()
        print('#' *50)
    return wrapper

@myDecorator
def myFunction():
    print("Hello, World!")

myFunction()
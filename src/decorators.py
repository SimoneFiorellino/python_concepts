"""
Creating a new function normally produces a callable object that executes its own code.

A decorator constructs a *wrapped* version of a function.

Python already uses decorators: functions like:
@staticmethod — A function inside a class that receives no automatic arguments. (no self or cls)
@classmethod — A method that receives the class (cls) instead of the instance.
@property — A method accessed like an attribute for computed or controlled values. (class.get_name())

-> Use a decorator when you want to enhance or modify how a function behaves,
   without changing the function's original source code.
"""

import time

def func(f):
    def wrapper(*args, **kwargs):
        """
        :param args: collects any number of non-keyword arguments into a tuple
        :param kwargs: collects any number of keyword arguments into a dictionary
        """
        print("Before function call")
        result = f(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{f.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@func
def greet():
    print("Hello, World!")

@func
def personal_greet(name):
    print(f"Hello, {name}!")

@func
def add(a, b):
    return a + b

@timer
def sleep_function(seconds):
    time.sleep(seconds)

greet()
personal_greet("Alice")
sum_result = add(5, 7)
print(f"Sum result: {sum_result}")

sleep_function(2)
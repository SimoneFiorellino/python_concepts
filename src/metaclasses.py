"""
Creating a new CLASS creates a new type of object, allowing new instances of that type to be made.

A metaclass constructs classes themselves.
This is powerful because you can, for example:
    1. enforce constraints
    2. modify attributes
    3. auto-register the class
    4. transform class definitions
    5. apply patterns automatically

Python already uses metaclasses: the default metaclass is 'type'.

-> Use a metaclass only when you want to modify or validate how classes are defined
"""


class Test:
    pass


print(type(Test))  # <class 'type'>

Test = type("Test", (), {"x": 5})  # equivalent to the class definition above

print(type(Test))  # <class 'type'>
print(Test.x)  # 5


##### Metaclass Example #####


class Meta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creating class {name} with Meta metaclass")

        a = {}
        for key, value in attrs.items():
            if key.startswith("__"):
                a[key] = value
            else:
                a[key.upper()] = value

        return type(name, bases, a)


class Person(metaclass=Meta):
    age = 25
    name = "John Doe"

    def greet(self):
        return f"Hello, my name is {self.NAME} and I am {self.AGE} years old."


p = Person()
print(p.GREET())  # Hello, my name is JOHN DOE and I am 25
print(p.NAME)  # JOHN DOE
print(p.AGE)  # 25

"""
Generators are a simple and powerful tool for creating iterators.
They are written like regular functions but use the yield statement whenever they want to return data.
"""


def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse("Hello"):
    print(char)


##### Generator Expressions #####

x = sum(i * i for i in range(10))  # sum of squares
print(x)

xvec = [10, 20, 30]
yvec = [7, 5, 3]
y = sum(x * y for x, y in zip(xvec, yvec))  # dot product
print(y)

data = "golf"
z = list(data[i] for i in range(len(data) - 1, -1, -1))  # reversed data as list
print(z)

z = list(char for char in reversed(data))  # using built-in reversed()
print(z)

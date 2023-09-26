"""
The operator @ in python is not implemented by default.
so you can use it to implement your own operator.
"""
class StringJoiner:
    def __init__(self, value):
        self.value = value

    def __matmul__(self, other):
        return self.value + "-" + other.value

# Using the @ operator
a = StringJoiner("Hello")
b = StringJoiner("World")
c = a @ b
assert c == "Hello-World"
# for debugging purposes you can get the name of a variable and its value
some_string = "wtfpython"
assert f"{some_string=}" == "some_string='wtfpython'"

"""
python has inside it numbers from -5 to 256
because these are common numbers and are used a lot
so two variables with the same number will point to the same
address in memory
"""
a = 256
b = 256
assert a is b


for line in """
a = 257
b = 257
assert a is not b
""".splitlines():
    print(f">>> {line}")
    exec(line)

"""
if you create the variables in the same line, with the same number
the interpreter is smart enough to create a single object in memory
an make the variables point to the same object
"""
for line in """
a, b = 257, 257
assert a is b
""".splitlines():
    print(f">>> {line}")
    exec(line)

"""
list are mutable so two list that are the same will point to different
address in memory
"""
a = []
b = []
assert a is not b

"""
however tuples are immutable so two tuples that are the same will not point
to the same address in memory
"""
a = tuple()
b = tuple()
assert a is b

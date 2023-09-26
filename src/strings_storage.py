import dis, sys

"""
strings can be interned, that means that the string is stored in a
table and the variable is just a reference to that string.
so if the strings are the same and are interned, the variables
will point to the same string in memory.
"""


def disssambler_wrapper():
    assert "strin" + "g" is "string"

    s1 = "strin"
    s2 = "string"
    assert s1 + "g" is not s2
    s3 = s1 + "g"
    assert s3 is not "string"
    assert sys.intern(s3) is "string"

    a = "some_string"
    assert id("some" + "_" + "string") == id(a)
    b = "some_string"
    assert a is b

    b = "_".join(["some", "string"])  # dynamically created string
    assert a is not b


print("bytescodes: \n")
disssambler_wrapper()
dis.dis(disssambler_wrapper)

"""
Strings that are not composed of ASCII letters, digits or underscores, are not interned
however because this code is run as strings.py the interpreter compile it before run it
and intern the strings.
"""
a = "wth!"
b = "wth!"
assert a is b

"""
this simulate the execution line by line so there is no compilation so the strings
are not interned
"""
for line in """
a = "wth!"
b = "wth!"
assert a is not b
""".splitlines():
    print(f">>> {line}")
    exec(line)

"""
because the strings are create in the same line, the interpreter intern the strings
"""
for line in """
a, b = "wth!", "wth!"
assert a is b
""".splitlines():
    print(f">>> {line}")
    exec(line)

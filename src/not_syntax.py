x = True
y = False

"""
https://docs.python.org/3/reference/expressions.html#operator-precedence
so == has higher precedence than not
assert not x == y is equivalent to assert not (x == y)
"""
assert False == False
assert not x == y
"""
SyntaxError
x == not y is equivalent to (x == not) y
and of course you cannot compare a boolean with a operator like not
"""
# x == not y

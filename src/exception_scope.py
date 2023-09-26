e = 7
try:
    raise Exception()
except Exception as e:
    pass

try:
    print(e)
except Exception as e:
    line_number = e.__traceback__.tb_lineno
    print(f"Caught an error at line {line_number}: {e}")

"""
https://docs.python.org/3/reference/compound_stmts.html#except
When an exception has been assigned using as target, it is cleared at the end of the except clause.
This is as if
except E as N:
  foo
was translated to
except E as N:
  try:
      foo
  finally:
      del N
This means the exception must be assigned to a different name to be able to refer to it after the except clause. Exceptions are cleared because with the traceback attached to them, they form a reference cycle with the stack frame, keeping all locals in that frame alive until the next garbage collection occurs.
"""

"""
In python exception clauses are not scoped, however function are scoped, so if you try to delete a variable
it delete the inner variable and not the outer one.
"""


def f(x):
    del x


x = 5
y = [5, 4, 3]
f(x)
f(y)
assert x == 5
assert y == [5, 4, 3]

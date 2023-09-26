def some_func():
    try:
        return "from_try"
    finally:
        return "from_finally"


def another_func():
    for _ in range(3):
        try:
            continue
        finally:
            print("Finally!")


# https://docs.python.org/3/reference/compound_stmts.html#finally-clause
def one_more_func():  # A gotcha!
    try:
        for i in range(3):
            try:
                1 / i
            except ZeroDivisionError:
                # If an exception occurs and is not handled, the exception is temporarily saved
                raise ZeroDivisionError("A trivial divide by zero error")
            #  If the finally clause executes a return, break or continue statement, the saved exception is discarded
            finally:
                print(f"Iteration {i}")
                break
    except ZeroDivisionError as e:
        print("Zero division error occurred", e)


"""
The return value of a function is determined by the last return statement executed. Since the finally clause always executes, a return statement executed in the finally clause will always be the last one executed
"""


def foo():
    try:
        return "try"
    finally:
        return "finally"


assert foo() == "finally"


assert some_func() == "from_finally"
print("another_func")
another_func()
print("one_more_func")
one_more_func()

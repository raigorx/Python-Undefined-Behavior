a = 1


def some_func():
    return a


"""
UnboundLocalError: local variable 'a' referenced before assignment

When you make an assignment to a variable in scope, it becomes local to that scope.
So a becomes local to the scope of another_func,
but it has not been initialized previously in the same scope, which throws an error.
"""


def another_func():
    a += 1
    return a


def some_closure_func():
    a = 1

    def some_inner_func():
        return a

    return some_inner_func()


"""
Here the a variable is not local to the scope of another_closure_func,
so the behavior is same as global variable.
"""


def another_closure_func():
    a = 1

    def another_inner_func():
        a += 1
        return a

    return another_inner_func()


assert some_func() == 1
assert some_closure_func() == 1

"""
To modify the outer scope variable a in another_func, we have to use the global keyword.
"""


def another_func_global():
    global a
    a += 1
    return a


assert another_func_global() == 2

"""
To modify the outer scope variable a in another_inner_func, use the nonlocal keyword.
The nonlocal statement is used to refer to variables defined in the nearest outer (excluding the global) scope.
"""


def another_func_nonlocal():
    a = 1

    def another_inner_func():
        nonlocal a
        a += 1
        return a

    return another_inner_func()


assert another_func_nonlocal() == 2

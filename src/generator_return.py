def some_func(x):
    if x == 3:
        return ["wtf"]
    else:
        yield from range(x)


assert list(some_func(3)) == []

"""
https://peps.python.org/pep-0380/#enhancements-to-stopiteration
In a generator, the statement
return value
is semantically equivalent to
raise StopIteration(value)
except that, as currently, the exception cannot be caught by except clauses within the returning generator.

In a function that contains a yield statement, return will essentially raise a StopIteration exception with return value as an argument.
of the exception
"""
some_string = None
try:
    next(some_func(3))
except StopIteration as e:
    some_string = e.value
assert some_string == ["wtf"]

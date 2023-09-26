import inspect

closures_funcs = []
closure_result_on_iteration = []
for x in range(7):

    def closure():
        return x

    closures_funcs.append(closure)
    closure_result_on_iteration.append(closure())

"""
the closure is created with the actual value of x
"""
assert closure_result_on_iteration == [0, 1, 2, 3, 4, 5, 6]

"""
on this case the closure remembers the last value of x
"""
closure_result_after_end = [func() for func in closures_funcs]
assert closure_result_after_end == [6, 6, 6, 6, 6, 6, 6]

gen_closures = []


def generate_numbers_with_closure():
    for x in range(7):

        def closure():
            return x

        gen_closures.append(closure)
        yield x


gen_instance = generate_numbers_with_closure()
next(gen_instance)
next(gen_instance)
next(gen_instance)
closure_result_after_end = [func() for func in gen_closures]
"""
another demostration that closures remember the last value of x
"""
assert closure_result_after_end == [2, 2, 2]

"""
the code creates a list of 10 lambda functions, however as the example mentioned
before the lambda functions remember the last value, and thats is 9 for this example
"""
powers_of_x = [lambda x: x**i for i in range(10)]
assert [f(2) for f in powers_of_x] == [512, 512, 512, 512, 512, 512, 512, 512, 512, 512]

"""
we can avoid the above problem by using a default argument
"""
powers_of_x = [lambda x, i=i: x**i for i in range(10)]
assert [f(2) for f in powers_of_x] == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]


closure_vars = inspect.getclosurevars(closures_funcs[0])
assert closure_vars.globals == {"x": 6}

"""
the closure variable is a global, so if you change the value of x
you change the result of the closure
"""
x = 42
assert [func() for func in closures_funcs] == [42, 42, 42, 42, 42, 42, 42]

"""
Here the variable is pass to the function as a named variable
so there is not a closure anymore
"""
funcs = []
for x in range(7):

    def some_func(x=x):
        return x

    funcs.append(some_func)

funcs_results = [func() for func in funcs]
assert funcs_results == [0, 1, 2, 3, 4, 5, 6]

closure_vars = inspect.getclosurevars(funcs[0])
assert closure_vars == inspect.ClosureVars(
    nonlocals={}, globals={}, builtins={}, unbound=set()
)

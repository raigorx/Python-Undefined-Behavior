import gc

array = [1, 8, 15]
"""
this is a literal tuple
(print(f"Checking {x} against array {array}"), array.count(x) > 0)
so [-1] is the last item of the tuple in this case is the result
of the expression array.count(x) > 0

https://docs.python.org/3/reference/expressions.html#generator-expressions
Variables used in the generator expression are evaluated lazily when the __next__() method is called for the generator object (in the same fashion as normal generators).
However, the iterable expression in the leftmost for clause is immediately evaluated.

its like gen were an object that its created with the actual array value
but in the time of the call it retrieves the value of array again and compare it
to the previous one.
"""
gen = (
    x
    for i, x in enumerate(array)
    if (
        print(
            f"list item in gen definition {x} list item in generator call {array[i]}"
        ),
        array.count(x) > 0,
    )[-1]
)
array = [2, 8, 22, 15]
assert list(gen) == [8, 15]

print("array_1")
array_1 = [1, 2, 3, 4]
"""
th iterable expression here (x for x in array_1)
is evaluated immediately on the creation of the generator
so the generator will contain the values of array_1 at the time of creation
"""
gen_1 = (
    x
    for i, x in enumerate(array_1)
    if (
        print(
            f"list item in gen definition {x} list item in generator call {array_1[i]}"
        ),
        True,
    )[-1]
)
array_1 = [1, 2, 3, 4, 5]


assert list(gen_1) == [1, 2, 3, 4]

print("array_2")
array_2 = [1, 2, 3, 4]
id_before = id(array_2)
gen_2 = (
    x
    for i, x in enumerate(array_2)
    if (
        print(
            f"list item in gen definition {x} list item in generator call {array_2[i]}"
        ),
        True,
    )[-1]
)
"""
this slice assignment change the list in place that means
no new object is created
"""
array_2[:] = [1, 2, 3, 4, 5]
id_after = id(array_2)
assert id_before == id_after


assert list(gen_2) == [1, 2, 3, 4, 5]

array_3 = [1, 2, 3]
array_4 = [10, 20, 30]
gen = (i + j for i in array_3 for j in array_4)

array_3 = [4, 5, 6]
array_4 = [400, 500, 600]

"""
https://peps.python.org/pep-0289/#the-details
Only the outermost for-expression is evaluated immediately, the other expressions are deferred until the generator is run.
so only (for i in array_3) is evaluated immediately and the rest are evaluated when the generator is run
"""
assert list(gen) == [401, 501, 601, 402, 502, 602, 403, 503, 603]

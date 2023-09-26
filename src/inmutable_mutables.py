some_tuple = ("A", "tuple", "with", "values")
another_tuple = ([1, 2], [3, 4], [5, 6])

try:
    some_tuple[2] = "change this"
except TypeError as e:
    line_number = e.__traceback__.tb_lineno
    print(f"Caught an error at line {line_number}: {e}")

another_tuple[2].append(1000)  # This throws no error
assert another_tuple == ([1, 2], [3, 4], [5, 6, 1000])

try:
    another_tuple[2] += [99, 999]
except TypeError as e:
    line_number = e.__traceback__.tb_lineno
    print(f"Caught an error at line {line_number}: {e}")
"""
https://docs.python.org/3/faq/programming.html#why-does-a-tuple-i-item-raise-an-exception-when-the-addition-works
"""
assert another_tuple == ([1, 2], [3, 4], [5, 6, 1000, 99, 999])

"""
this is an example of what happend above, the tuple[n] is mutated and after it
is assigned but because tuples are inmutable it throws an error
"""
a_tuple = (["foo"], "bar")
result = a_tuple[0].__iadd__(["item"])
assert result == ["foo", "item"]
assert a_tuple == (["foo", "item"], "bar")
try:
    a_tuple[0] = result
except TypeError as e:
    line_number = e.__traceback__.tb_lineno
    print(f"Caught an error at line {line_number}: {e}")

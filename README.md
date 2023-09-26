# Python-Undefined-Behavior

Inspired from <https://github.com/satwikkansal/wtfpython>.

The names comes from C++ where the behavior of the program is hard to predict or being unpredictable,
this is usually has a syntax that trick the programmer to think in a certain way but the program does
something unexpected.
<details><summary>addition_assignment_operator.py</summary>

```py
"""
a = a + [5, 6, 7, 8]
is not the same as
a += [5, 6, 7, 8]

the assigment operator = create a new variable and assign it to the variable name
the += operator mutate the variable in place.
"""
a = [1, 2, 3, 4]
b = a
assert b is a
previous_a_id = id(a)
a = a + [5, 6, 7, 8]
assert id(b) == previous_a_id
assert b is not a
assert a == [1, 2, 3, 4, 5, 6, 7, 8]
assert b == [1, 2, 3, 4]

a = [1, 2, 3, 4]
b = a
a += [5, 6, 7, 8]
assert a is b
assert a == [1, 2, 3, 4, 5, 6, 7, 8]
assert b == [1, 2, 3, 4, 5, 6, 7, 8]

```
</details>

<details><summary>all_conditional.py</summary>

```py
"""
This a simple example of the all() function in python.
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
"""

assert all([True, True, True])

assert all([True, True, False]) is False

"""
empty iterable is True
This behavior aligns with a principle in mathematics, where an empty set
has one element, the empty set itself.
"""
assert all([])

"""
False because the passed list has one element, [], and in python, an empty list is falsy
"""
assert all([[]]) is False
assert bool([]) is False

"""
higher recursive variants are always True.
This is because the passed array's single element ([[...]]) is no longer empty,
and lists with values are truthy
"""
assert all([[[]]])

```
</details>

<details><summary>assertion_syntax.py</summary>

```py
a = "python"
b = "javascript"
assert (a == b, "Both languages are different")
"""
above is being evaluated as a tuple, below an example
"""
assert (False, True)
assert a != b

```
</details>

<details><summary>base_class.py</summary>

```py
assert isinstance(3, int)
assert isinstance(type, object)
assert isinstance(object, type)


class A:
    pass


assert isinstance(A, A) is False
assert isinstance(type, type)
assert isinstance(object, object)

assert issubclass(int, object)
assert issubclass(type, object)
assert issubclass(object, type) is False

# 1. All classes are either direct or indirect subclasses of 'object'.
assert issubclass(int, object)
assert issubclass(float, object)
assert issubclass(list, object)
assert issubclass(dict, object)
assert issubclass(str, object)
assert issubclass(type, object)

assert not object.__bases__

# 2. For most classes, 'object' is at the end of their method resolution order (MRO).
assert int.mro()[-1] == object
assert float.mro()[-1] == object
assert list.mro()[-1] == object

# For 'type' and 'object', they have a special relationship.
# 'type' is an instance of itself and 'object' is an instance of 'type'.
# Their MROs reflect their unique relationship.
assert type.mro(type) == [type, object]
assert object.mro() == [object]

```
</details>

<details><summary>booleans_are_integers.py</summary>

```py
assert bool(1.0) is True
assert bool(0.0) is False
assert bool("some_string") is True
assert bool(0) is False
assert bool([]) is False

assert int(True) == 1
assert int(False) == 0
"""
so bools are integers
"""
assert "wth" * True == "wth"
assert "wth" * False == ""

assert issubclass(bool, int)

assert issubclass(int, bool) is False

assert isinstance(True, int)

assert isinstance(False, int)

```
</details>

<details><summary>chained_operations.py</summary>

```py
"""
https://docs.python.org/3/reference/expressions.html#comparisons
Unlike C, all comparison operations in Python have the same priority

Formally, if a, b, c, …, y, z are expressions and op1, op2, …, opN are comparison operators,
then a op1 b op2 c ... y opN z is equivalent to a op1 b and b op2 c and ... y opN z,
except that each expression is evaluated at most once.

What this means is
x < y <= z
is equivalent to
x < y and y <= z
"""
import dis


def disssambler_wrapper():
    assert False is False is False

    assert not (False == False) in [False]

    assert not (False == (False in [False]))

    assert False == False and False in [False]
    """
    The below assert is equivalent to the above assert
    """
    assert False == False in [False]

    assert True is (False == False)

    assert not ((True is False) and (False == False))
    """
    The below assert is equivalent to the above assert
    """
    assert not (True is False == False)

    assert False is False is False

    assert 1 > 0 < 1

    assert not (1 > 0) < 1

    assert not 1 > (0 < 1)


print("bytescodes: \n")
disssambler_wrapper()
dis.dis(disssambler_wrapper)

```
</details>

<details><summary>circular_reference.py</summary>

```py
"""
{5: ({...}, 5)}
the ... means circular reference in other words
{...} is {5: (, 5)}
"""
a, b = a[b] = {}, 5
assert a == {5: (a, 5)}
assert a[5][0] is a
assert a[5][0] == {5: (a, 5)}

"""
same as above but in multiple lines for simpler understanding
"""
a, b = {}, 5
a[5] = a, 5
assert a == {5: (a, 5)}
assert a[5][0] is a

"""
similar to above but instead of using the same single dict(a) its using
two different dicts, so no circular reference
"""
a, b = {}, 5
a[b] = {}, 5
assert a == {5: ({}, 5)}

a = []
b = [a]
a.append(b)
# RecursionError: maximum recursion depth exceeded in comparison
# assert a[0][0][0][0] == [[[a]]]

"""
more examples of circular reference
"""
some_list = some_list[0] = [0]
assert some_list == [[some_list]]
assert some_list[0] == [[some_list]]
assert some_list is some_list[0]
assert some_list[0][0][0][0][0][0] == some_list
assert some_list[0][0][0][0][0][0] is some_list

```
</details>

<details><summary>class_instance_attr_lookup.py</summary>

```py
class A:
    x = 1


class B(A):
    pass


class C(A):
    pass


assert {A: A.x, B: B.x, C: C.x} == {A: 1, B: 1, C: 1}


B.x = 2
assert {A: A.x, B: B.x, C: C.x} == {A: 1, B: 2, C: 1}

A.x = 3
"""
C.x changed, but B.x didn't
Thats is because x doesn't exist in C, so python looks for it in its parent(A)
B has its own x from previous assigment, so it doesn't need to look for it in its parent(A)

Method Resolution Order (MRO).
This dictates the order in which base classes are searched
when looking for a method (or attribute) in a class
"""
assert "x" in B.__dict__  # True if B has its own 'x', False otherwise
assert "x" not in C.__dict__
assert B.mro() == [B, A, object]  # from left to right it looks for x
assert C.mro() == [C, A, object]
assert {A: A.x, B: B.x, C: C.x} == {A: 3, B: 2, C: 3}

"""
the instance itself doesn't have x, so it looks for it in its class
"""
a = A()
assert "x" not in a.__dict__
assert type(a).mro() == [A, object]
assert {"instance_a": a.x, "class_a": A.x} == {"instance_a": 3, "class_a": 3}

a.x = 4
assert "x" in a.__dict__
assert {"instance_a": a.x, "class_a": A.x} == {"instance_a": 4, "class_a": 3}


del B.x
a = A()
b = B()
c = C()
"""
The operator += on attributes doesn't change any other class or instance
"""
C.x += 5
c.x += 5
assert {
    "inst_a": a.x,
    "class_a": A.x,
    "inst_b": b.x,
    "class_b": B.x,
    "inst_c": c.x,
    "class_c": C.x,
} == {"inst_a": 3, "class_a": 3, "inst_b": 3, "class_b": 3, "inst_c": 13, "class_c": 8}


class SomeClass:
    some_var = 15
    some_list = [5]
    another_list = [5]

    def __init__(self, x):
        self.some_var = x + 1
        self.some_list = self.some_list + [x]
        self.another_list += [x]


some_obj = SomeClass(420)
assert some_obj.some_list == [5, 420]
assert some_obj.another_list == [5, 420]

"""
The += operator modifies the attribute object in-place without creating a new attribute
so no new attribute is created in the instance and the lookup is done in the class
"""
another_obj = SomeClass(111)
assert another_obj.some_list == [5, 111]
assert another_obj.another_list == [5, 420, 111]
assert some_obj.another_list == [5, 420, 111]

assert another_obj.another_list is SomeClass.another_list is some_obj.another_list

```
</details>

<details><summary>class_scope_ignoring.py</summary>

```py
"""
Scopes nested inside class definition ignore names bound at the class level.
generators expressions and list comprehensions have their own scope.
"""
import inspect

x = 5


class SomeClass:
    x = 17
    y = (x for i in range(10))
    z = [x for i in range(10)]

    def method():
        return x


generate_list = list(SomeClass.y)
assert generate_list == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
generate_list = list(SomeClass.z)
assert generate_list == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
assert SomeClass.method() == 5

```
</details>

<details><summary>closure.py</summary>

```py
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

```
</details>

<details><summary>conditional_expression_syntax.py</summary>

```py
"""
reminder: ternary operator also called conditional expression
value_if_the_condition_is_true if condition_to_evaluate else value_if_the_condition_is_false
"""
x, y = (0, 1) if True else None, None
# expected x,y == (0, 1)
assert x == (0, 1)
assert y is None
assert (x, y) == ((0, 1), None)
"""
this is what happended first tuple is assigned to x, then y is assigned to None
"""
x = (0, 2) if True else None
assert x == (0, 2)

# if you want the expected result you have to do
x, y = (0, 1) if True else (None, None)
assert (x, y) == (0, 1)

```
</details>

<details><summary>custom_operator.py</summary>

```py
"""
The operator @ in python is not implemented by default.
so you can use it to implement your own operator.
"""
class StringJoiner:
    def __init__(self, value):
        self.value = value

    def __matmul__(self, other):
        return self.value + "-" + other.value

# Using the @ operator
a = StringJoiner("Hello")
b = StringJoiner("World")
c = a @ b
assert c == "Hello-World"
# for debugging purposes you can get the name of a variable and its value
some_string = "wtfpython"
assert f"{some_string=}" == "some_string='wtfpython'"

```
</details>

<details><summary>default_arg_mutable.py</summary>

```py
def some_func(default_arg=[]):
    default_arg.append("some_string")
    return default_arg


assert some_func() == ["some_string"]
assert some_func() == ["some_string", "some_string"]
"""
in the below code, we are passing an empty list, so the default argument becomes
the empty list, and the function appends the "some_string" to the empty list.

so yes the default argument persists across function calls
"""
assert some_func([]) == ["some_string"]
"""
here again we are not passing any argument, so the default argument is used
"""
assert some_func() == ["some_string", "some_string", "some_string"]


def some_func_new(default_arg=[]):
    default_arg.append("some_string")
    return default_arg


assert some_func_new.__defaults__ == ([],)
some_func_new()
assert some_func_new.__defaults__ == (["some_string"],)
some_func_new()
assert some_func_new.__defaults__ == (["some_string", "some_string"],)
assert some_func_new([]) == ["some_string"]
assert some_func_new.__defaults__ == (["some_string", "some_string"],)

"""
common fix for this behavior
"""


def some_func_fix(default_arg=None):
    if default_arg is None:
        default_arg = []
    default_arg.append("some_string")
    return default_arg

```
</details>

<details><summary>del_magic_method.py</summary>

```py
import sys

del_count = 0


class SomeClass:
    def __del__(self):
        global del_count
        del_count += 1
        print("deleted", self)


x = SomeClass()
y = x
# This will be 3, because:
# 2 for x and y,
# plus 1 for being an argument to getrefcount
assert sys.getrefcount(x) - 1 == 2
del x
assert sys.getrefcount(y) - 1 == 1
assert del_count == 0
del y
assert del_count == 1


x = SomeClass()
y = x
del x
assert del_count == 1
# assert "y" in globals()
del y
assert del_count == 2
print(globals())

"""
if you put the script below into the python interpreter line by line
you will see a different result, because the momement you type "y"
to see its value a reference to is is created an store to the magic variable _
so when you do "del y"
a reference to y still exist in the magic variable, but when you execute an expression
like globals() the magic variable _ is updated an now "y" no longer has reference
triggering the __del__ method
"""
"""
import sys
del_count = 0


class SomeClass:
    def __del__(self):
        global del_count
        del_count += 1
        print("deleted", self)

x = SomeClass()
y = x
# This will be 3, because:
# 2 for x and y,
# plus 1 for being an argument to getrefcount
assert sys.getrefcount(x) - 1 == 2
del x
y
assert sys.getrefcount(y) - 1 == 2
assert del_count == 0
del y
assert del_count == 0
globals()
assert del_count == 1
"""

```
</details>

<details><summary>dictionary_key.py</summary>

```py
class SomeClass(str):
    pass


some_dict = {"s": 42}
dict_keys = list(some_dict.keys())[0]
assert type(dict_keys) == str
"""
Since SomeClass inherits from str, when you pass the string "s" to it,
then the str constructor is called.
you're essentially constructing an object that is similar to a string with the value "s"
"""
s = SomeClass("s")
some_dict[s] = 40
"""
because SomeClass is a subclass of str, the equality operator is inherited from str
as the __hash__ too.
as a reminder, the __hash__ method is used to create keys in a dictionary.
"""
assert s == "s"
assert some_dict == {"s": 40}
"""
because "s" and s are the same key, this dictionary
is essentially the same as the one above.
"""
assert some_dict == {"s": 40, s: 40}

"""
here the equality operator is change so it not being inherited from str
"""


class SomeClassTampered(str):
    def __eq__(self, other):
        return (
            type(self) is SomeClass
            and type(other) is SomeClass
            and super().__eq__(other)
        )

    # When we define a custom __eq__, Python stops automatically inheriting the
    # __hash__ method, so we need to define it as well
    __hash__ = str.__hash__


some_dict = {"s": 42}
s = SomeClassTampered("s")
some_dict[s] = 40
assert some_dict == {"s": 42, s: 40}

keys = list(some_dict.keys())
assert isinstance(keys[0], str)
assert isinstance(keys[1], SomeClassTampered)

```
</details>

<details><summary>dict_keys.py</summary>

```py
"""
python does implicit type conversion
so 5 becomes 5.0 and 5.0 becomes 5 + 0j
"""
assert 5 == 5.0 == 5 + 0j

"""
https://docs.python.org/3/library/functions.html#hash
Return the hash value of the object (if it has one). Hash values are integers.
They are used to quickly compare dictionary keys during a dictionary lookup.
Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).
"""
assert hash(5) == hash(5.0) == hash(5 + 0j)

"""
of course those are not the same object
"""
assert 5 is not 5.0 is not 5 + 0j


some_dict = {}
some_dict[5.5] = "JavaScript"
some_dict[5.0] = "Ruby"
some_dict[5] = "Python"

assert some_dict[5.5] == "JavaScript"
assert some_dict[5.0] == "Python"
assert some_dict[5] == "Python"

complex_five = 5 + 0j
assert type(complex_five) == complex
assert some_dict[complex_five] == "Python"

some_dict = {}
some_dict[5] = "Ruby"
assert (5.0 in some_dict) and (5 + 0j in some_dict)
assert str(some_dict) == "{5: 'Ruby'}"

some_dict[5.0] = "JavaScript"
assert str(some_dict) == "{5: 'JavaScript'}"

del some_dict[5.0]
some_dict[5.0] = "C++"
assert str(some_dict) == "{5.0: 'C++'}"

```
</details>

<details><summary>dict_order.py</summary>

```py
from collections import OrderedDict

"""
Curly braces or the set() function can be used to create sets.
Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary
"""
assert type({}) == dict
assert type(set()) == set


dictionary = dict()
dictionary[1] = "a"
dictionary[2] = "b"

ordered_dict = OrderedDict()
ordered_dict[1] = "a"
ordered_dict[2] = "b"

another_ordered_dict = OrderedDict()
another_ordered_dict[2] = "b"
another_ordered_dict[1] = "a"


class DictWithHash(dict):
    """
    A dict that also implements __hash__ magic.
    """

    __hash__ = lambda self: 0


class OrderedDictWithHash(OrderedDict):
    """
    An OrderedDict that also implements __hash__ magic.
    """

    __hash__ = lambda self: 0


assert dictionary == ordered_dict

assert dictionary == another_ordered_dict

"""
https://docs.python.org/3/library/collections.html#ordereddict-objects
Equality tests between OrderedDict objects are order-sensitive and are implemented as list(od1.items())==list(od2.items()).
Equality tests between OrderedDict objects and other Mapping objects are order-insensitive like regular dictionaries.
This allows OrderedDict objects to be substituted anywhere a regular dictionary is used.
"""
assert ordered_dict != another_ordered_dict

# {obj1, obj2, obj3} in python is a literal for set
assert type({"apple", "banana", "cherry"}) == set

try:
    len({dictionary, ordered_dict, another_ordered_dict})
except TypeError as e:
    print(f"dict don't have __hash__ implemented {e}")

dictionary = DictWithHash()
dictionary[1] = "a"
dictionary[2] = "b"

ordered_dict = OrderedDictWithHash()
ordered_dict[1] = "a"
ordered_dict[2] = "b"

another_ordered_dict = OrderedDictWithHash()
another_ordered_dict[2] = "b"
another_ordered_dict[1] = "a"

"""
because dictionary is equal to ordered_dict and another_ordered_dict
and its inserted first in the set, the set will contain only one object
however if dictionary is inserted last the two ordered_dict will be compared
and they are not equal so the set will contain two objects
"""
assert len({dictionary, ordered_dict, another_ordered_dict}) == 1
assert len({ordered_dict, another_ordered_dict, dictionary}) == 2

some_set = set()
some_set.add(dictionary)
assert ordered_dict in some_set

some_set.add(ordered_dict)
assert len(some_set) == 1

assert another_ordered_dict in some_set

some_set.add(another_ordered_dict)
assert len(some_set) == 1


another_set = set()
another_set.add(ordered_dict)
assert another_ordered_dict not in another_set

another_set.add(another_ordered_dict)
assert len(another_set) == 2

assert dictionary in another_set

another_set.add(another_ordered_dict)
assert len(another_set) == 2

```
</details>

<details><summary>ellipsis.py</summary>

```py
def some_func():
    assert Ellipsis

some_func()

assert ... is Ellipsis

"""
Ellipsis can be use as pass
"""
def yet_to_be_implemented_function():
    ...
"""
type-hint as reminder type hint are suggestion not enforcement
on this example its specified that the tuple can be any length
with float values
"""
from typing import Tuple
VectorND = Tuple[float, ...]  # any number of float values or integer or wathever
v1: VectorND = (1.0, 2.0)
v2: VectorND = (0, 5, "hello")
v3: VectorND = (1.0,)


"""
ellipsis can be use as sentinel value too
"""
def process_data(data, preprocess=None):
    if preprocess is Ellipsis:
        # Do some default preprocessing
        print("Default preprocessing!")
```
</details>

<details><summary>else_for_exception.py</summary>

```py
"""
else can be used with for loops
"""


def does_exists_num(l, to_find):
    result = ""
    for num in l:
        if num == to_find:
            result = "Exists!"
            break
    else:
        result = "Does not exist"
    return result


some_list = [1, 2, 3, 4, 5]
assert does_exists_num(some_list, 4) == "Exists!"
assert does_exists_num(some_list, -1) == "Does not exist"

"""
else clause after a try block is also called "completion clause" as reaching the else clause in a try statement means that the try block actually completed successfully.
"""
result = ""
try:
    pass
except:
    result = "Exception occurred!!!"
else:
    result = "Try block executed successfully..."

assert result == "Try block executed successfully..."

```
</details>

<details><summary>empty_tuple_list_syntax.py</summary>

```py
[] = () #valid syntax unpack empty tuple
```
</details>

<details><summary>escape_backslash_strings.py</summary>

```py
print("\\")
print(r"\"")
"""
on raw string backslash is passed as itself literal and on the same time
it escapes the next character

so r"wt\"f" is "wt\f" escaping the " on the same time introducing \ as a character

This means when a parser encounters a backslash in a raw string, it expects another character following it.
And in our case (print(r"\")), the backslash escaped the trailing quote,
leaving the parser without a terminating quote (hence the SyntaxError).
That's why backslashes don't work at the end of a raw string.
"""
assert r"wt\"f" == 'wt\\"f'
assert r"\\n" == "\\\\n"

"""
\ escaped the next character and that means the close " is gone
so to make it works we need to add the missing "
"""
# r"\"
r"\""

```
</details>

<details><summary>exception_scope.py</summary>

```py
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

```
</details>

<details><summary>exception_syntax.py</summary>

```py
some_list = [1, 2, 3]
try:
    # This should raise an ``IndexError``
    print(some_list[4])
# Old syntax python 2
# except IndexError, ValueError:
#    print("Caught!")
except (IndexError, ValueError) as e:
    print("Caught!")
    print(e)

try:
    # This should raise a ``ValueError``
    some_list.remove(4)
except (IndexError, ValueError) as e:
    print("Caught again!")
    print(e)

```
</details>

<details><summary>finally.py</summary>

```py
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

```
</details>

<details><summary>for_loop_assigment.py</summary>

```py
some_string = "wth"
some_dict = {}
for iter, some_dict[iter] in enumerate(some_string):
    iter = 10
    assert iter == 10

"""
the assignment in the for loop is equivalent to:
"""
assert some_dict == {0: "w", 1: "t", 2: "h"}
"""
however i= 10 doesnt have the expected effect because
everytime the loop is executed iter is assigned a new value from
enumerate(some_string) and the assignment iter = 10 is overwritten
"""

```
</details>

<details><summary>for_loop_scope.py</summary>

```py
"""
python for loop iterator variable scope it's define in global scope
"""
for x in range(7):
    pass
assert x == 6
assert "x" in globals()

y = -1
for y in range(7):
    pass
assert y == 6
assert "y" in globals()

```
</details>

<details><summary>generator.py</summary>

```py
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

```
</details>

<details><summary>generator_return.py</summary>

```py
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

```
</details>

<details><summary>implicit_conversion_boolean.py</summary>

```py
"""
Python has an undocumented converse implication operator.
If you replace False and True by 0 and 1 and do the maths,
the truth table is equivalent to a converse implication operator
"""
assert False ** False == True
assert False ** True == False
assert True ** False == True
assert True ** True == True
```
</details>

<details><summary>infinity_float.py</summary>

```py
"""
just as curiosity the hash of infinity float is pi
"""
assert hash(float('infinity')) == 314159
assert hash(float('-inf')) == -314159
```
</details>

<details><summary>inmutable_mutables.py</summary>

```py
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

```
</details>

<details><summary>int_characters.py</summary>

```py
#https://chris.improbable.org/2014/8/25/adventures-in-unicode-digits/
assert int('١٢٣٤٥٦٧٨٩') == 123456789
```
</details>

<details><summary>int_string_conversion_limit.py</summary>

```py
import sys

"""
https://docs.python.org/3/library/stdtypes.html#int-max-str-digits
There exists no algorithm that can convert a string to a binary integer or a binary integer to a string in linear time
Converting a large value such as int('1' * 500_000) can take over a second on a fast CPU.
"""
try:
    int("2" * 5432)
except ValueError as e:
    line_number = e.__traceback__.tb_lineno
    print(f"Caught an error at line {line_number}: {e}")

"""
however you can change the limit of the conversion
"""
sys.set_int_max_str_digits(7000)
int("2" * 5432)

```
</details>

<details><summary>is_is_not.py</summary>

```py
import operator

"""
(is not operator) is a single operator
but (is) and (not) are two different operators
"""
assert ("something" is not None) == operator.is_not("something", None)

assert ("something" is (not None)) == operator.is_("something", (not None))

```
</details>

<details><summary>is_operator.py</summary>

```py
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

```
</details>

<details><summary>iteration_change.py</summary>

```py
"""
change iterator while iterating is not allowed in python
"""

x = {0: None}

for i in x:
    x[i + 1] = None

```
</details>

<details><summary>iteration_delete.py</summary>

```py
list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]

"""
del var_name just removes the binding of the var_name from the local or global namespace (That's why the list_1 is unaffected).
"""
for idx, item in enumerate(list_1):
    assert "item" in locals()
    del item
    assert "item" not in locals()
    assert "list_1" in globals()


"""
The list iteration is done index by index, and when we remove. The remaining elements are shifted down, i.e., 2 is at index 0, and 3 is at index 1. Since the next iteration is going to look at index 1 (which is the 3), the 2 gets skipped entirely.
A similar thing will happen with every alternate element in the list sequence.
"""
for idx, item in enumerate(list_2):
    print(f"Index: {idx}, Item: {item}, List before removal: {list_2}")
    list_2.remove(item)
    print(f"List after removal: {list_2}")

"""
slices create a copy of the list, so the iteration is not affected by the removal of elements.
"""
some_list = [1, 2, 3, 4]
assert some_list[:] is not some_list
for idx, item in enumerate(list_3[:]):
    list_3.remove(item)

"""
same behavior as list_2.remove
"""
for idx, item in enumerate(list_4):
    print(f"Index: {idx}, Item: {item}, List before removal: {list_4}")
    list_4.pop(idx)
    print(f"List after removal: {list_4}")

assert list_1 == [1, 2, 3, 4]
assert list_2 == [2, 4]
assert list_3 == []
assert list_4 == [2, 4]

```
</details>

<details><summary>list_dict_in_place.py</summary>

```py
some_list = [1, 2, 3]
some_dict = {"key_1": 1, "key_2": 2, "key_3": 3}

some_list = some_list.append(4)
some_dict = some_dict.update({"key_4": 4})

"""
append and update modify the list and dict in place, and return None
"""
assert some_list is None
assert some_dict is None

```
</details>

<details><summary>list_multiply.py</summary>

```py
row = [""] * 3

board = [row] * 3

assert board[0] == ["", "", ""]
assert board[0][0] == ""
assert board == [["", "", ""], ["", "", ""], ["", "", ""]]

board[0][0] = "X"

assert id(row) == id(board[0]) == id(board[1]) == id(board[2])

assert board == [["X", "", ""], ["X", "", ""], ["X", "", ""]]

row[0] = "O"

assert board == [["O", "", ""], ["O", "", ""], ["O", "", ""]]

board = [[""] * 3 for _ in range(3)]
board[0][0] = "X"

assert board == [["X", "", ""], ["", "", ""], ["", "", ""]]

```
</details>

<details><summary>list_slicing_bound.py</summary>

```py
"""
List slicing with out of the bounds indices throws no errors
"""
some_list = [1, 2, 3, 4, 5]
assert some_list[111:] == []
```
</details>

<details><summary>list_syntax_comma.py</summary>

```py
ten_words_list = ["1", "2", "3", "4", "5" "6", "7", "8", "9", "10"]
"""
missing comma means string concatenation
"""
assert len(ten_words_list) == 9

```
</details>

<details><summary>method_equality_identity.py</summary>

```py
import types


class CallableClass:
    def __call__(self):
        return 2 * 2


class SomeClass:
    def method(self):
        print(f"method called with self: {self}")
        # return 3**3

    @classmethod
    def class_method(cls):
        print(f"class_method called with self: {cls}")

    @staticmethod
    def static_method():
        pass


"""
In Python, a descriptor is an object attribute with "binding behavior",
one whose attribute access has been overridden by methods in the descriptor protocol.
These methods are __get__(), __set__(), and __delete__().
If an object defines any of these methods, it's considered a descriptor.

let's manually invoke the descriptor mechanism:
"""
bound_func = SomeClass.method.__get__(CallableClass)
"""
bound_func is a bound method object
"""
assert isinstance(bound_func, types.MethodType)
"""
the parameter pass to __get__ is the self that receives the method call
"""
assert getattr(bound_func, "__self__") == CallableClass
bound_func()

"""
methods accessed through the class are not bound to an object
so no self is passed
"""
assert not hasattr(SomeClass.method, "__self__")

obj1 = SomeClass()
obj2 = SomeClass()

assert bound_func.__self__ != obj1.method.__self__
"""
obj1.method creates a new method object each time it is accessed
that makes it have a different identity(address)
obj1.method this create an object
obj1.method() this calls the object
"""
assert isinstance(obj1.method, types.MethodType)
assert obj1.method is not obj1.method

"""
However accessing the method through the class does not create a new object
that makes it have the same identity(address)
"""
assert not isinstance(SomeClass.method, types.MethodType)
assert SomeClass.method is SomeClass.method

"""
@classmethod creates a method object when accessed through the class too
that makes it have a different identity(address)

Class methods are descriptors that, when accessed,
create a method object which are passed as the first argument the class(cls)
instead of an instance(self)
"""
assert SomeClass.class_method is not SomeClass.class_method
assert SomeClass.class_method == SomeClass.class_method
assert hasattr(SomeClass.class_method, "__self__")
assert obj1.class_method is not obj1.class_method

"""
@staticmethod does not create a method object when accessed through the class
that makes it have the same identity(address)
"""
assert SomeClass.static_method is SomeClass.static_method
assert obj1.static_method is obj1.static_method
assert (
    obj1.static_method
    is obj1.static_method
    is obj2.static_method
    is SomeClass.static_method
)

"""
the == operator checks value equality. For the bound method objects,
their __eq__ method is implemented to check if the method's function (__func__) and the bound object (__self__) are equal.

so obj1 and obj2 have same (__func__) but different (__self__)
"""
assert obj1.method != obj2.method

"""
obj1 and obj2 have same (__func__) and same (cls)
same for SomeClass.class_method
"""
assert obj1.method == obj1.method
assert obj1.class_method == obj1.class_method
assert obj1.class_method == obj2.class_method

"""
the above assertions as one
"""
assert (
    obj1.class_method
    == obj1.class_method
    == obj2.class_method
    == SomeClass.class_method
)

```
</details>

<details><summary>multiprocessing_sample.py</summary>

```py
import multiprocessing
import time

def cpu_bound_task(n):
    while n > 0:
        n -= 1
"""
compare to threads the multiprocessing spawn a new process and each process has its own GIL
so the CPU-bound task can be executed in parallel
"""
if __name__ == '__main__':
    start = time.time()
    processes = []
    # Create 2 processes that run a CPU-bound task
    for _ in range(2):
        process = multiprocessing.Process(target=cpu_bound_task, args=(10**8,))
        process.start()
        processes.append(process)

    # Wait for both processes to complete
    for process in processes:
        process.join()

    end = time.time()
    multiprocessing_time = (end - start)
    start = time.time()
    cpu_bound_task(10**8)
    cpu_bound_task(10**8)
    end = time.time()
    non_multiprocessing_time = (end - start)
    print(f"cpu bound task {multiprocessing_time=}")
    print(f"cpu bound task {non_multiprocessing_time=}")
    assert multiprocessing_time < non_multiprocessing_time
```
</details>

<details><summary>name_mangling.py</summary>

```py
# https://en.wikipedia.org/wiki/Name_mangling

class Yo(object):
    def __init__(self):
        self.__honey = True
        self.bro = True

assert Yo().bro
try:
    Yo().__honey
except AttributeError as e:
    print(f"{e}")
"""
In Python, the interpreter modifies (mangles) the class member
names starting with __ (double underscore a.k.a "dunder") and not ending with
more than one trailing underscore by adding _NameOfTheClass in front.
"""
assert Yo()._Yo__honey
assert "_Yo__honey" in Yo().__dict__

class Yo_second(object):
    def __init__(self):
        # Let's try something symmetrical this time
        self.__honey__ = True
        self.bro = True

assert Yo_second().bro
try:
  Yo_second()._Yo__honey__
except AttributeError as e:
  print(f"{e}")

assert "__honey__" in Yo_second().__dict__

_A__variable = "Some value"

class A(object):
    def some_func(self):
        return __variable # not initialized anywhere yet

# __variable is mangle to _A__variable
assert A().some_func() == "Some value"

try:
  A().__variable
except AttributeError as e:
  print(f"{e}")

assert "__variable" not in A().__dict__

```
</details>

<details><summary>nan_infinity.py</summary>

```py
import math

assert (math.nan == math.nan) is False

assert float("inf") == math.inf

assert math.isnan(float("nan"))

assert float("-iNf") == -math.inf

assert float("inf") == -float("-inf")

assert 50 / math.inf == 0.0

assert math.isnan(math.inf / math.inf)

assert math.isnan(23 + math.nan)

y = math.nan / math.nan
assert y is y
assert y != y
"""
In containers python first check if its contents identity is same and if that is the case
it makes it true, so no == operator comparasion is done.
"""
assert [y] == [y]
x = math.nan
assert x != y
assert [x] != [y]

```
</details>

<details><summary>not_syntax.py</summary>

```py
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

```
</details>

<details><summary>numeric_separators.py</summary>

```py
six_million = 6_000_000
assert six_million == 6000000
hex_address = 0xF00D_CAFE
assert hex_address == 4027435774
```
</details>

<details><summary>object_id.py</summary>

```py
class EXAMPLE:
    pass


"""
python compare objectt by identity not their content
Since EXAMPLE() creates a new instance each time it's called
these two instances are different objects with different memory addresses.
"""
assert EXAMPLE() != EXAMPLE()

"""
The is operator checks for object identity (i.e., if two references refer to the same object in memory).
"""
assert EXAMPLE() is not EXAMPLE()

"""
In Python, by default, the hash() of an object is derived from its id(), which is unique for distinct objects and ensures different memory addresses.
But there's a catch: the hash of short-lived objects (objects that are quickly created and destroyed, like in this case) can be reused.
"""
assert hash(EXAMPLE()) == hash(EXAMPLE())


class SAMPLE:
    def __init__(self):
        print(f"Constructor {id(self)}")

    def __del__(self):
        print(f"Destructor {id(self)}")


"""
The order of objeect creation and destruction is what makes the difference
between id and (is operator)
in id the object is created and destroyed before the call to id
but in (is operator) both objects are created the is operator is called
and after it the objects are destroyed.

And the last key point is that Cpython use the same memory address for the
newly created object if the previous object is destroyed.
"""
print("id == id")
assert id(SAMPLE()) == id(SAMPLE())
print("SAMPLE is SAMPLE")
assert SAMPLE() is not SAMPLE()

```
</details>

<details><summary>object_size_in_memory.py</summary>

```py
"""
the __dict__ size in memory is implementation defined and can change between versions
here you can observer surprise behavior from the perpective of the programmer
test in 3.11.4 64 bits python windows
"""
import sys

class SomeClass:
    def __init__(self):
        self.some_attr1 = 1
        self.some_attr2 = 2
        self.some_attr3 = 3
        self.some_attr4 = 4


def dict_size(o):
    return sys.getsizeof(o.__dict__)

o1 = SomeClass()
o2 = SomeClass()
o1_size = dict_size(o1)
o2_size = dict_size(o2)
# normal expected behavior
assert o1_size == o2_size

del o1.some_attr1
o3 = SomeClass()
recalculate_o1_size = dict_size(o1)
# expected because an attribute was deleted
assert recalculate_o1_size != o1_size

o3_size = dict_size(o3)
# o1 was modified however is equal to o3
assert o3_size == recalculate_o1_size
# only o1 was modified however the 3 dicts are equal
assert dict_size(o3) == dict_size(o1) == dict_size(o2)

o1 = SomeClass()
o2 = SomeClass()
old_o1_size = dict_size(o1)
o1.some_attr5 = 5
o1.some_attr6 = 6
assert dict_size(o1) == old_o1_size
assert dict_size(o1) == dict_size(o2)
o3 = SomeClass()
assert dict_size(o3) == dict_size(o1) == dict_size(o2)
```
</details>

<details><summary>packing_unpacking.py</summary>

```py
def get_variable_name(variable):
    return [name for name, value in globals().items() if value is variable][0]


# packing
packed = 1, 2, 3, 4
isinstance(packed, tuple) and print(f"{get_variable_name(packed)} is a tuple!")

# Unpacking the tuple into variables
one, two, three, four = packed
assert one == packed[0]
assert two == packed[1]
assert three == packed[2]
assert four == packed[3]

# Extended Unpacking
first, *middle, last = packed
assert first == packed[0]
assert middle == list(packed[1:-1])
assert last == packed[-1]

```
</details>

<details><summary>plus_plus_operator.py</summary>

```py
"""
There is no ++ operator in Python grammar. It is actually two + operators.
++a parses as +(+a) which translates to a.
Similarly, the output of the statement --a can be justified.
"""
assert 3 --0-- 5 == 8
assert 3 + 0 + 5 == 8
assert --5 == 5
temp = --5
assert temp == 5
```
</details>

<details><summary>print_after.py</summary>

```py
import time

"""
This will print the wtfpython after 3 seconds due to the end argument because the output buffer is flushed either after encountering \n or when the program finishes execution. We can force the buffer to flush by passing flush=True argument.
"""
print("wthpython", end="_")
time.sleep(2)

print()
print("python_fix", end="_", flush=True)
time.sleep(2)
```
</details>

<details><summary>recursion_in_place.py</summary>

```py
result = []


def some_recursive_func(a):
    if a[0] == 0:
        return
    a[0] -= 1
    some_recursive_func(a)
    result.append(a)
    return a


"""
the recursion decrement a[0] until it reaches 0
and return it so [5, 0] becomes [0, 0]
the result return in every recursion is [0, 0]
because the operator -= modify the list in place
"""
assert some_recursive_func([5, 0]) == [0, 0]
assert result == [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

result = []


def similar_recursive_func(a):
    if a == 0:
        return a
    a -= 1
    similar_recursive_func(a)
    result.append(a)
    return a


"""
here the recursion decrement a until it reaches 0
but because integers are non-mutable the operator -= doesn't modify it in place
"""
assert similar_recursive_func(5) == 4
assert result == [0, 1, 2, 3, 4]

```
</details>

<details><summary>round_banker.py</summary>

```py
def get_middle(some_list):
    mid_index = round(len(some_list) / 2)
    return some_list[mid_index - 1]


"""
get_middle([1]) only returned 1 because the index was round(0.5) - 1 = 0 - 1 = -1
returning the last element in the list.
"""
assert get_middle([1]) == 1
assert get_middle([1, 2, 3]) == 2
"""
This is not a float precision error, in fact, this behavior is intentional. Since Python 3.0, round() uses banker's rounding where .5 fractions are rounded to the nearest even number
This is the recommended way to round .5 fractions as described in IEEE 754. However,
the most popular programming languages (for example: JavaScript, Java, C/C++, Ruby, Rust) do not use banker's rounding either
"""
assert get_middle([1, 2, 3, 4, 5]) == 2
assert round(0.5) == 0
assert round(1.5) == 2
assert round(2.5) == 2
assert len([1, 2, 3, 4, 5]) / 2 == 2.5
assert round(len([1, 2, 3, 4, 5]) / 2) == 2

```
</details>

<details><summary>same_letter_different.py</summary>

```py
"""
Some non-Western characters look identical to letters in the English
alphabet but are considered distinct by the interpreter.
"""
value = 11
valuе = 32
assert value == 11

assert ord('е') == 1077# cyrillic 'e' (Ye)

assert ord('e') == 101# latin 'e', as used in English and typed using standard keyboard
assert 'е' != 'e'

value = 42 # latin e
valuе = 23 # cyrillic 'e', Python 2.x interpreter would raise a `SyntaxError` here
assert value == 42

```
</details>

<details><summary>scope_variable.py</summary>

```py
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

```
</details>

<details><summary>secrets.py</summary>

```py
from __future__ import barry_as_FLUFL

# from __future__ import braces
# SyntaxError: not a chance
"""
#https://github.com/python/cpython/blob/025eb98dc0c1dc27404df6c544fc2944e0fa9f3a/Python/future.c#L49
The __future__ module is normally used to provide features from future versions of Python. The "future" in this specific context is however, ironic.
"""

"""
this works only in interactive mode that is why eval is used
"""
print(eval('"Ruby" <> "Python"'))

from antigravity import *

# https://github.com/python/cpython/blob/main/Lib/antigravity.py#L7-L17
geohash(37.421542, -122.085589, b"2005-05-26-10458.68")

# Zen of Python!
import this

```
</details>

<details><summary>single_char_type.py</summary>

```py
"""
In python doesn't exist single character type like char in C
so every single character is a string
so 'b'[0] evaluate to an string
"""
assert isinstance('a'[0][0][0][0][0], str)
assert 'a'[0][0][0][0][0] == 'a'

```
</details>

<details><summary>slicing_new_object.py</summary>

```py
some_str = "wthpython"
some_list = ['w', 't', 'h', 'p', 'y', 't', 'h', 'o', 'n']
assert some_list is not some_list[:] # False expected because a new object is created.
assert some_str is some_str[:] # True because strings are immutable, so making a new object is of not much use.

```
</details>

<details><summary>sorted.py</summary>

```py
"""
The sorted method always returns a list, and comparing lists and tuples always returns False in Python.
"""
assert [] != tuple()
x = 7, 8, 9
assert isinstance(x, tuple)
assert isinstance(x, list) is False
assert sorted(x) == [7, 8, 9]
assert sorted(x) != x
assert sorted(x) == sorted(x)

y = reversed(x)
assert hasattr(y, "__iter__")
assert hasattr(y, "__next__")
assert sorted(y) == [7, 8, 9]
assert sorted(y) == []
y = reversed(x)
assert sorted(y) != sorted(y)

```
</details>

<details><summary>space_invader_operator.py</summary>

```py
a = 42
"""
Explanation: This prank comes from https://twitter.com/raymondh/status/1131103570856632321?lang=en
The space invader operator is actually just a malformatted a -= (-1).
Which is equivalent to a = a - (- 1). Similar for the a += (+ 1) case.
"""
a -=- 1
assert a == 43
"""
same operator as above
"""
a = 42
a -= (-1)
assert a == 43
a = 42
a = a - (- 1)
assert a == 43
a = 42
a += (+ 1)
assert a == 43
```
</details>

<details><summary>split.py</summary>

```py
"""
https://docs.python.org/3/library/stdtypes.html#str.split
"""
assert "a".split() == ["a"]
assert "a".split(" ") == ["a"]

assert len("".split()) == 0
assert "".split() == []
assert len("".split(" ")) == 1
"""
Splitting an empty string with a specified separator returns ['']
"""
assert "".split(" ") == [""]

assert " a ".split(" ") == ["", "a", ""]
assert " a ".split() == ["a"]

```
</details>

<details><summary>strings_storage.py</summary>

```py
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

```
</details>

<details><summary>string_count.py</summary>

```py
"""
https://docs.python.org/3/library/stdtypes.html#str.count
If sub is empty, returns the number of empty strings between characters which is the length of the string plus one.
"""
assert 'abc'.count('') == 4
```
</details>

<details><summary>subclass_relationships.py</summary>

```py
"""
Python Subclass Relationships Aren't Transitive

Transitive is a term that often refers to a relationship where
if A relates to B and B relates to C
then A necessarily relates to C.
"""
from collections.abc import Hashable


a, b, c = 1, 2, 3

assert a < b
assert b < c
# Due to transitivity of '<', we can infer:
assert a < c


assert issubclass(list, object)

assert issubclass(object, Hashable)

assert issubclass(list, Hashable) is False
assert "__hash__" in dir(list)
assert getattr(list, "__hash__") is None


# A hashable class (by default)
class HashableClass:
    pass


assert "__hash__" in dir(HashableClass)
assert hasattr(HashableClass, "__hash__")


# A class that explicitly sets __hash__ to None, making it unhashable
class UnhashableClass:
    __hash__ = None


# A subclass that inherits from an unhashable class
class ChildOfUnhashable(UnhashableClass):
    pass


assert issubclass(HashableClass, Hashable)
assert issubclass(UnhashableClass, Hashable) is False
assert issubclass(ChildOfUnhashable, Hashable) is False

```
</details>

<details><summary>thread.py</summary>

```py
import threading
import time
import http.client
import ssl

def cpu_bound_task(n):
    while n > 0:
        n -= 1

start = time.time()
threads = []
# Create 2 threads that run a CPU-bound task
for _ in range(2):
    thread = threading.Thread(target=cpu_bound_task, args=(10**8,))
    thread.start()
    threads.append(thread)

# Wait for both threads to complete
for thread in threads:
    thread.join()

end = time.time()
thread_time = (end - start)
start = time.time()
cpu_bound_task(10**8)
cpu_bound_task(10**8)
end = time.time()
non_thread_time = (end - start)
"""
Multiple Python threads won't run your Python code concurrently (yes, you heard it right!).
It may seem intuitive to spawn several threads and let them execute your Python code concurrently, but, because of the Global Interpreter Lock in Python, all you're doing is making your threads execute on the same core turn by turn.
so case like this threads just make it slower instead of faster.

However these can lead to unexpected results so, some times is the opposite
thread_time < non_thread_time
these example is a CPU-bound one
"""
print(f"cpu bound task {thread_time=}")
print(f"cpu bound task {non_thread_time=}")

def fetch_website(url):
    domain = url.replace("https://", "").replace("http://", "")
    conn = http.client.HTTPSConnection(domain, context=ssl._create_unverified_context())
    conn.request("GET", "/")
    response = conn.getresponse()
    response.read().decode()
    conn.close()

websites = ['https://www.google.com', 'https://www.bing.com']

start = time.time()

threads = []
for website in websites:
    thread = threading.Thread(target=fetch_website, args=(website,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

IO_thread_time = (end - start)
start = time.time()
for website in websites:
    fetch_website(website)
end = time.time()
non_IO_thread_time = (end - start)
"""
In IO-bound tasks, threads improve perfomance because the GIL is released while waiting for the IO operation to complete.
"""
assert non_IO_thread_time > IO_thread_time

```
</details>

<details><summary>triple_quoted_strings.py</summary>

```py
print('wthpython''')
#above same as
print('wthpython' '') #this is a concatenation of two strings
print('wthpython' 'AB')
print("wthpython""")

"""
The following statements raise `SyntaxError`
python treat triple quoted strings as string delimiters
so if you start a triple quoted string, you need to end it
"""
# print('''wtfpython')
# print("""wtfpython")

```
</details>

<details><summary>tuple_iteration_syntax.py</summary>

```py
def tuple_sample():
    t = ("one", "two")
    result = []
    for i in t:
        result.append(i)
    return result


def tuple_str_sample():
    t = ('one')
    result = []
    for i in t:
        result.append(i)
    return result


t = ()
assert isinstance(t, tuple)

assert tuple_sample() == ["one", "two"]
"""
python interpreter ('one') as string not as tuple
for turn it into a tuple you need to do ('one',)
"""
assert tuple_str_sample() == ["o", "n", "e"]
assert isinstance(('one'), str)
assert isinstance(('one',), tuple)
```
</details>

<details><summary>warlus.py</summary>

```py
a = "wth_walrus"


def angle(phi):
    pass


"""
It's invalid with the porpuse of avoid visual confusion with
the assignment operator.
a = "wth_walrus"
besides in these cases is better to use the assignment operator
"""
# a := "wth_walrus"
# lat = a := 0

# angle(phi = lat := 59.9)

# def distance(phi = lat := 0, lam = lon := 0):
#     pass

"""
however with parentheses the syntax become valid, although
the assignment operator is not necessary, bringing just confusion
"""
(a := "wth_walrus")

lat = (a := 0)

angle(phi=(lat := 59.9))


def distance(phi=(lat := 0), lam=(lon := 0)):
    pass


a = 6, 9
assert a == (6, 9)

a, b = 6, 9
# (a, b = 16, 19) # invalid syntax

# unexpected 3-tuple
(a, b := 16, 19)
assert a == 6
assert b == 16

assert (a := 6, 9) == ((a := 6), 9)
x = (a := 696, 9)
assert x[0] is a

"""
In Formatted String Literals (f-strings) the syntax :=
can be missunderstood as the warlus operator but it's
the Format Specification Mini-Language
https://docs.python.org/3/library/string.html#format-string-syntax
what you put after the colon(:) is the format specifier
https://docs.python.org/3/library/string.html#formatspec

the = is the alignment specifier
Forces the padding to be placed after the sign (if any) but before the digits.
This is used for printing fields in the form ‘+000000120’.
This alignment option is only valid for numeric types.
It becomes the default for numbers when ‘0’ immediately precedes the field width.
"""
number = 3
assert f"{number:=4}" == "   3"

text = "hello"
"""
as it's mentioned above the aligment specifier is only valid for numeric types
so it's invalid to use it with text
"""
# f"{text:=8}"  # invalid syntax

"""
again if you use parentheses it becomes the warlus operator
"""
assert f"{(text:=8)}" == "8"

# SyntaxError: cannot use assignment expressions with subscript
# (mapping["hearts"] := "♥")

# SyntaxError: cannot use assignment expressions with attribute
# (number.answer := 42)

# SyntaxError: invalid syntax
# lat, lon := 59.9, 10.8

# SyntaxError: invalid syntax
# count +:= 1

lat = 0
assert (lat, lon := 59.9, 10.8) == (0, 59.9, 10.8)

"""
When assigning a tuple using the walrus operator, you always need to use parentheses around the tuple
"""
walrus = 3.7, False
(walrus := 1, True)
assert walrus == 1
(walrus := (1, True))
assert walrus == (1, True)

```
</details>

<details><summary>zip_iterator.py</summary>

```py
numbers = list(range(7))
assert numbers == [0, 1, 2, 3, 4, 5, 6]
first_three, remaining = numbers[:3], numbers[3:]
assert first_three == [0, 1, 2]
assert remaining == [3, 4, 5, 6]
numbers_iter = iter(numbers)
assert list(iter(numbers)) == [0, 1, 2, 3, 4, 5, 6]
assert list(zip(numbers_iter, first_three)) == [(0, 0), (1, 1), (2, 2)]

assert list(zip(numbers_iter, remaining)) == [(4, 3), (5, 4), (6, 5)]
"""
Where did element 3 go from the numbers_iter?
in previous iteration the numbers_iter was called but first_three was exhausted, so the numbers_iter was at index 3
which is discarded because the first_three is exhausted.
"""

"""
however if you put the first_three first it will works because
the iterator numbers_iters is not called because the first_three is exhausted first
"""
numbers_iter = iter(numbers)
assert list(zip(first_three, numbers_iter)) == [(0, 0), (1, 1), (2, 2)]
assert list(zip(remaining, numbers_iter)) == [(3, 3), (4, 4), (5, 5), (6, 6)]

```
</details>

### import_wildcard
<details><summary>import_wildcard.py</summary>

```py
"""
It is often advisable to not use wildcard imports.
in wildcard imports, the names with a leading underscore don't get imported.
"""

from module_error import *
from module_fix import *

assert some_weird_name_func_() == "works!"
try:
    _another_weird_name_func()
except NameError:
    print("The function _another_weird_name_func is not defined.")

assert some_weird_name_func_fix() == "works!"
assert _another_weird_name_func_fix() == "works!"

```
</details>

<details><summary>module_error.py</summary>

```py
# File: module_error.py


def some_weird_name_func_():
    return "works!"


def _another_weird_name_func():
    return "works!"

```
</details>

<details><summary>module_fix.py</summary>

```py
# File: module_fix.py

__all__ = ["_another_weird_name_func_fix", "some_weird_name_func_fix"]


def some_weird_name_func_fix():
    return "works!"


def _another_weird_name_func_fix():
    return "works!"

```
</details>


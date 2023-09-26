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

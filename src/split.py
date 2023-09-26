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

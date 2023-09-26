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

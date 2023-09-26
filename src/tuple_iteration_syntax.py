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
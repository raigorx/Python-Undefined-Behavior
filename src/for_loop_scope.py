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

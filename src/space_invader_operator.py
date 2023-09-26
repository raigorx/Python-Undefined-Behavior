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
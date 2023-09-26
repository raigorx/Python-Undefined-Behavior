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
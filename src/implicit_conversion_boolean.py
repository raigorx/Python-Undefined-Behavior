"""
Python has an undocumented converse implication operator.
If you replace False and True by 0 and 1 and do the maths,
the truth table is equivalent to a converse implication operator
"""
assert False ** False == True
assert False ** True == False
assert True ** False == True
assert True ** True == True
import operator

"""
(is not operator) is a single operator
but (is) and (not) are two different operators
"""
assert ("something" is not None) == operator.is_not("something", None)

assert ("something" is (not None)) == operator.is_("something", (not None))

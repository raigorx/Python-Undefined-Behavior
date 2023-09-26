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

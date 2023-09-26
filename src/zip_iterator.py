numbers = list(range(7))
assert numbers == [0, 1, 2, 3, 4, 5, 6]
first_three, remaining = numbers[:3], numbers[3:]
assert first_three == [0, 1, 2]
assert remaining == [3, 4, 5, 6]
numbers_iter = iter(numbers)
assert list(iter(numbers)) == [0, 1, 2, 3, 4, 5, 6]
assert list(zip(numbers_iter, first_three)) == [(0, 0), (1, 1), (2, 2)]

assert list(zip(numbers_iter, remaining)) == [(4, 3), (5, 4), (6, 5)]
"""
Where did element 3 go from the numbers_iter?
in previous iteration the numbers_iter was called but first_three was exhausted, so the numbers_iter was at index 3
which is discarded because the first_three is exhausted.
"""

"""
however if you put the first_three first it will works because
the iterator numbers_iters is not called because the first_three is exhausted first
"""
numbers_iter = iter(numbers)
assert list(zip(first_three, numbers_iter)) == [(0, 0), (1, 1), (2, 2)]
assert list(zip(remaining, numbers_iter)) == [(3, 3), (4, 4), (5, 5), (6, 6)]

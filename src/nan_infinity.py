import math

assert (math.nan == math.nan) is False

assert float("inf") == math.inf

assert math.isnan(float("nan"))

assert float("-iNf") == -math.inf

assert float("inf") == -float("-inf")

assert 50 / math.inf == 0.0

assert math.isnan(math.inf / math.inf)

assert math.isnan(23 + math.nan)

y = math.nan / math.nan
assert y is y
assert y != y
"""
In containers python first check if its contents identity is same and if that is the case
it makes it true, so no == operator comparasion is done.
"""
assert [y] == [y]
x = math.nan
assert x != y
assert [x] != [y]

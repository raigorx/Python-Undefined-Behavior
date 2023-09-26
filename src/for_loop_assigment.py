some_string = "wth"
some_dict = {}
for iter, some_dict[iter] in enumerate(some_string):
    iter = 10
    assert iter == 10

"""
the assignment in the for loop is equivalent to:
"""
assert some_dict == {0: "w", 1: "t", 2: "h"}
"""
however i= 10 doesnt have the expected effect because
everytime the loop is executed iter is assigned a new value from
enumerate(some_string) and the assignment iter = 10 is overwritten
"""

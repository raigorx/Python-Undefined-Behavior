"""
else can be used with for loops
"""


def does_exists_num(l, to_find):
    result = ""
    for num in l:
        if num == to_find:
            result = "Exists!"
            break
    else:
        result = "Does not exist"
    return result


some_list = [1, 2, 3, 4, 5]
assert does_exists_num(some_list, 4) == "Exists!"
assert does_exists_num(some_list, -1) == "Does not exist"

"""
else clause after a try block is also called "completion clause" as reaching the else clause in a try statement means that the try block actually completed successfully.
"""
result = ""
try:
    pass
except:
    result = "Exception occurred!!!"
else:
    result = "Try block executed successfully..."

assert result == "Try block executed successfully..."

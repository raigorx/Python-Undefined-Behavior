list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]

"""
del var_name just removes the binding of the var_name from the local or global namespace (That's why the list_1 is unaffected).
"""
for idx, item in enumerate(list_1):
    assert "item" in locals()
    del item
    assert "item" not in locals()
    assert "list_1" in globals()


"""
The list iteration is done index by index, and when we remove. The remaining elements are shifted down, i.e., 2 is at index 0, and 3 is at index 1. Since the next iteration is going to look at index 1 (which is the 3), the 2 gets skipped entirely.
A similar thing will happen with every alternate element in the list sequence.
"""
for idx, item in enumerate(list_2):
    print(f"Index: {idx}, Item: {item}, List before removal: {list_2}")
    list_2.remove(item)
    print(f"List after removal: {list_2}")

"""
slices create a copy of the list, so the iteration is not affected by the removal of elements.
"""
some_list = [1, 2, 3, 4]
assert some_list[:] is not some_list
for idx, item in enumerate(list_3[:]):
    list_3.remove(item)

"""
same behavior as list_2.remove
"""
for idx, item in enumerate(list_4):
    print(f"Index: {idx}, Item: {item}, List before removal: {list_4}")
    list_4.pop(idx)
    print(f"List after removal: {list_4}")

assert list_1 == [1, 2, 3, 4]
assert list_2 == [2, 4]
assert list_3 == []
assert list_4 == [2, 4]

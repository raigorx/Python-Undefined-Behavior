some_list = [1, 2, 3]
try:
    # This should raise an ``IndexError``
    print(some_list[4])
# Old syntax python 2
# except IndexError, ValueError:
#    print("Caught!")
except (IndexError, ValueError) as e:
    print("Caught!")
    print(e)

try:
    # This should raise a ``ValueError``
    some_list.remove(4)
except (IndexError, ValueError) as e:
    print("Caught again!")
    print(e)

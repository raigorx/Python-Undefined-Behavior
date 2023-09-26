import sys

"""
https://docs.python.org/3/library/stdtypes.html#int-max-str-digits
There exists no algorithm that can convert a string to a binary integer or a binary integer to a string in linear time
Converting a large value such as int('1' * 500_000) can take over a second on a fast CPU.
"""
try:
    int("2" * 5432)
except ValueError as e:
    line_number = e.__traceback__.tb_lineno
    print(f"Caught an error at line {line_number}: {e}")

"""
however you can change the limit of the conversion
"""
sys.set_int_max_str_digits(7000)
int("2" * 5432)

"""
Some non-Western characters look identical to letters in the English
alphabet but are considered distinct by the interpreter.
"""
value = 11
valuе = 32
assert value == 11

assert ord('е') == 1077# cyrillic 'e' (Ye)

assert ord('e') == 101# latin 'e', as used in English and typed using standard keyboard
assert 'е' != 'e'

value = 42 # latin e
valuе = 23 # cyrillic 'e', Python 2.x interpreter would raise a `SyntaxError` here
assert value == 42

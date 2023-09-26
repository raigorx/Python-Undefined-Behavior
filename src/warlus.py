a = "wth_walrus"


def angle(phi):
    pass


"""
It's invalid with the porpuse of avoid visual confusion with
the assignment operator.
a = "wth_walrus"
besides in these cases is better to use the assignment operator
"""
# a := "wth_walrus"
# lat = a := 0

# angle(phi = lat := 59.9)

# def distance(phi = lat := 0, lam = lon := 0):
#     pass

"""
however with parentheses the syntax become valid, although
the assignment operator is not necessary, bringing just confusion
"""
(a := "wth_walrus")

lat = (a := 0)

angle(phi=(lat := 59.9))


def distance(phi=(lat := 0), lam=(lon := 0)):
    pass


a = 6, 9
assert a == (6, 9)

a, b = 6, 9
# (a, b = 16, 19) # invalid syntax

# unexpected 3-tuple
(a, b := 16, 19)
assert a == 6
assert b == 16

assert (a := 6, 9) == ((a := 6), 9)
x = (a := 696, 9)
assert x[0] is a

"""
In Formatted String Literals (f-strings) the syntax :=
can be missunderstood as the warlus operator but it's
the Format Specification Mini-Language
https://docs.python.org/3/library/string.html#format-string-syntax
what you put after the colon(:) is the format specifier
https://docs.python.org/3/library/string.html#formatspec

the = is the alignment specifier
Forces the padding to be placed after the sign (if any) but before the digits.
This is used for printing fields in the form ‘+000000120’.
This alignment option is only valid for numeric types.
It becomes the default for numbers when ‘0’ immediately precedes the field width.
"""
number = 3
assert f"{number:=4}" == "   3"

text = "hello"
"""
as it's mentioned above the aligment specifier is only valid for numeric types
so it's invalid to use it with text
"""
# f"{text:=8}"  # invalid syntax

"""
again if you use parentheses it becomes the warlus operator
"""
assert f"{(text:=8)}" == "8"

# SyntaxError: cannot use assignment expressions with subscript
# (mapping["hearts"] := "♥")

# SyntaxError: cannot use assignment expressions with attribute
# (number.answer := 42)

# SyntaxError: invalid syntax
# lat, lon := 59.9, 10.8

# SyntaxError: invalid syntax
# count +:= 1

lat = 0
assert (lat, lon := 59.9, 10.8) == (0, 59.9, 10.8)

"""
When assigning a tuple using the walrus operator, you always need to use parentheses around the tuple
"""
walrus = 3.7, False
(walrus := 1, True)
assert walrus == 1
(walrus := (1, True))
assert walrus == (1, True)

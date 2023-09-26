print("\\")
print(r"\"")
"""
on raw string backslash is passed as itself literal and on the same time
it escapes the next character

so r"wt\"f" is "wt\f" escaping the " on the same time introducing \ as a character

This means when a parser encounters a backslash in a raw string, it expects another character following it.
And in our case (print(r"\")), the backslash escaped the trailing quote,
leaving the parser without a terminating quote (hence the SyntaxError).
That's why backslashes don't work at the end of a raw string.
"""
assert r"wt\"f" == 'wt\\"f'
assert r"\\n" == "\\\\n"

"""
\ escaped the next character and that means the close " is gone
so to make it works we need to add the missing "
"""
# r"\"
r"\""

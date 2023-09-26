"""
change iterator while iterating is not allowed in python
"""

x = {0: None}

for i in x:
    x[i + 1] = None

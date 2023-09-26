class A:
    x = 1


class B(A):
    pass


class C(A):
    pass


assert {A: A.x, B: B.x, C: C.x} == {A: 1, B: 1, C: 1}


B.x = 2
assert {A: A.x, B: B.x, C: C.x} == {A: 1, B: 2, C: 1}

A.x = 3
"""
C.x changed, but B.x didn't
Thats is because x doesn't exist in C, so python looks for it in its parent(A)
B has its own x from previous assigment, so it doesn't need to look for it in its parent(A)

Method Resolution Order (MRO).
This dictates the order in which base classes are searched
when looking for a method (or attribute) in a class
"""
assert "x" in B.__dict__  # True if B has its own 'x', False otherwise
assert "x" not in C.__dict__
assert B.mro() == [B, A, object]  # from left to right it looks for x
assert C.mro() == [C, A, object]
assert {A: A.x, B: B.x, C: C.x} == {A: 3, B: 2, C: 3}

"""
the instance itself doesn't have x, so it looks for it in its class
"""
a = A()
assert "x" not in a.__dict__
assert type(a).mro() == [A, object]
assert {"instance_a": a.x, "class_a": A.x} == {"instance_a": 3, "class_a": 3}

a.x = 4
assert "x" in a.__dict__
assert {"instance_a": a.x, "class_a": A.x} == {"instance_a": 4, "class_a": 3}


del B.x
a = A()
b = B()
c = C()
"""
The operator += on attributes doesn't change any other class or instance
"""
C.x += 5
c.x += 5
assert {
    "inst_a": a.x,
    "class_a": A.x,
    "inst_b": b.x,
    "class_b": B.x,
    "inst_c": c.x,
    "class_c": C.x,
} == {"inst_a": 3, "class_a": 3, "inst_b": 3, "class_b": 3, "inst_c": 13, "class_c": 8}


class SomeClass:
    some_var = 15
    some_list = [5]
    another_list = [5]

    def __init__(self, x):
        self.some_var = x + 1
        self.some_list = self.some_list + [x]
        self.another_list += [x]


some_obj = SomeClass(420)
assert some_obj.some_list == [5, 420]
assert some_obj.another_list == [5, 420]

"""
The += operator modifies the attribute object in-place without creating a new attribute
so no new attribute is created in the instance and the lookup is done in the class
"""
another_obj = SomeClass(111)
assert another_obj.some_list == [5, 111]
assert another_obj.another_list == [5, 420, 111]
assert some_obj.another_list == [5, 420, 111]

assert another_obj.another_list is SomeClass.another_list is some_obj.another_list

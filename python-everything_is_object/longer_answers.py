# fmt: off

# QUESTION 16
def inc(n):
    n += 1
a = 1
inc(a)
print(f"16: {a}")
"""
Cause n is getting an immutable also n is inside the function scope of inc, because
inc doesn't return the value of n += 1, it just creates a new object and increments
inside it, you'd use something like a = inc(1) for a = 2 in the global scope.
"""


# QUESTION 17
def inc2(n):
    n.append(4)
l = [1, 2, 3]
inc2(l)
print(f'17: {l}')
"""
cause `l` is a list (mutable) we are passing inc2 a reference to that list. I think it's
called passing as argument or something like that. In essence both `l` and the argument `n`
point to the same object.
"""

# QUESTION 18
def assign_value(n, v):
    n = v
l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(f"18: {l1}")
"""
Same as before, we passing references but because they are pointers to pointers, when we
change the assignement of n we changing to what it points, inside assign_value n now points to v
which in turn points to l2. we're just changing to what it points.
"""

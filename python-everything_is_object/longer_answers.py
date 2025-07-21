# fmt: off

# QUESTION 9
# What do these 3 lines print?
s1_9 = "Best School"
s2_9 = "Best School"
print(f"9: s1_9 is s2_9? {s1_9 is s2_9}")
"""
So in essence, python does whatever the fuck it wants
sometimes it will return false and sometimes true.
"""


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


# QUESTION 20
"""
a = ()
Is a a tuple? Answer with Yes or No.

Yes, I remembed you need to specify set() if you want to define an empty set. or use other function
I dont remember which xD because it would create an empty tumple instead.
"""


# QUESTION 22
"""
a = (1)
Is a a tuple? Answer with Yes or No.

I got this wrong, turns out it's just a empty integer with parenthesis, you need trailing comma
for it to be a tuple.
"""

# QUESTION 25
a = (1, 2)
b = (1, 2)
print(f"25: {a is b}")
"""
A: Sometimes true sometimes false.
Also got this wrong, turns out the python guy would intern simpler tuples, but not larger tuples.
Just python being python. And in fact sometimes it does sometimes it doesn't.
"""

# QUESTION 26
a = ()
b = ()
print(f"26: {a is b}")
"""
A: True
Simples tuples are interned to same object.
"""

# QUESTION 27
#Will the last line of this script print the same ID as before?
a_27 = [1, 2, 3, 4]
a_27_id_before = id(a_27)
print(f"27: {a_27}")
a_27 = a_27 + [5]
a_27_id_after = id(a_27)
print(f"27: Is ID same? {a_27_id_after == a_27_id_before}")
"""
Concat creates a new list.
"""

# QUESTION 28
a_28 = [1, 2, 3]
a_28_id_before = id(a_28)
a_28 += [4]
print(f"28: does a_28 hold its previous ID? {id(a_28) == a_28_id_before}")

"""
The difference is in how = vs += operates.
In 27: 'a_27 +' creates a new array and concats the element '5' to that new array which holds a copy of a_27
then that is assigned to a_27.
In 28 everything is done in place.
"""

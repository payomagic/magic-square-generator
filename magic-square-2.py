import random

# get inputs from spectators
p = random.randint(1, 12)
z = random.randint(1, 12)

# generate random sum n between 18 and 49
n = random.randint(18, 49)

# calculate remaining numbers based on magic square template
a = p
b = n - 10
c = 7
d = n - 4
e = n - 11
f = 6
g = n - 5
h = 9
i = 2
j = n - 2
k = 3
l = n - 7
m = 12
n1 = 5
o = n - 20
p1 = z

# print out magic square
print("+-----+-----+-----+-----+")
print("|  {}  |  {}  |  {}  |  {}  |".format(a, b, c, d))
print("+-----+-----+-----+-----+")
print("|  {}  |  {}  |  {}  |  {}  |".format(e, f, g, h))
print("+-----+-----+-----+-----+")
print("|  {}  |  {}  |  {}  |  {}  |".format(i, j, k, l))
print("+-----+-----+-----+-----+")
print("|  {} |  {}  |  {}  |  {}  |".format(m, n1, o, p1))
print("+-----+-----+-----+-----+")

def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    return res
# ? res = 31


print(s(10, 11))

print(s(11, 10, 10))

# print(s(b=31))
# TypeError: s() missing 1 required positional argument: 'a'

# print(s(b=31.0))
# TypeError: s() missing 1 required positional argument: 'a'

print(s(5, 5, 5, 5, 1))

print(s(11, 10, b=10))

print(s(0, 0, 31))

print(s(21))

print(s(11, b=20))

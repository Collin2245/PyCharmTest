import timeit


@profile
def gcd_loop(n, m):
    if m == 0:
        return 0
    l = n % m
    while l > 0:
        n = m
        m = l
        l = n % m
    return m


@profile
def gcd_recursion(n, m):
    if m == 0:
        return n
    else:
        l = n % m
        n = m
        m = l
        return gcd_recursion(n, m)


def test_loop():
    gcd_loop(21312423432, 12324332214)


def test_recursion():
    gcd_recursion(21312423432, 12324332214)


test_loop()
test_recursion()
print(timeit.Timer(test_loop).timeit(number=300))
print(timeit.Timer(test_recursion).timeit(number=300))

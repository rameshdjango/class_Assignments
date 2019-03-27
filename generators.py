# Generator function:
def gen(a, y=0, z=1):
    """

    :param a: a holds the value
    :param y: y holds the 0
    :param z: z = 1
    :return: return the a value ordering
    """
# if y < a then swapping a, y
    if y < a:
        a, y = y, a
    while a < y:
        yield a
        a += z


ans = gen(5)
print ans.next()
print ans.next()

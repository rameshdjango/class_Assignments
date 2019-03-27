def gen(n):
    a = 0
    while a < n:
        yield a
        a += 1


x = gen(5)
for i in range(5):
    print x.next()

# or
di_ct = [{"name": "siva", "marks": 100}, {"name": "rams", "marks": 20},
         {"name": "reddy", "marks": 500}]
di_ct.sort()
print di_ct

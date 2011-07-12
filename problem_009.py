def is_pythagorean(a, b, c):
    return a ** 2 +  b ** 2 == c ** 2

assert is_pythagorean(3, 4, 5) == True
assert is_pythagorean(3, 4, 10) == False

def get_result():
    for c in xrange(1, 1000):
        for b in xrange(1, c):
            for a in xrange(1, b):
                if a + b + c == 1000 and is_pythagorean(a, b, c):
                    return a * b * c

result = get_result()
print 'Result: %d' % result

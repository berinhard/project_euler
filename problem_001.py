def get_sum_in_range(r):
    return sum(x for x in xrange(r) if not x % 3 or not x % 5)

assert get_sum_in_range(10) == 23

result = get_sum_in_range(1000)
print 'Result: %d' % result
assert result == 233168

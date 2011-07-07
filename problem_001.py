def get_sum_in_range(r):
    return sum(x for x in xrange(r) if not x % 3 or not x % 5)

assert get_sum_in_range(10) == 23

print 'Result: %d' % get_sum_in_range(1000)

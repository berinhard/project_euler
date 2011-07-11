def is_prime(number):
    if number == 1 or number == 2:
        return True

    if not number % 2:
        return False

    for i in xrange(3, int(number ** 0.5) + 1, 2):
        if not number % i:
            return False

    return True

def largest_prime_factor(number):
    factors = [n for n in xrange(1, int(number ** 0.5) + 1) if not number % n]
    factors.reverse()

    for factor in factors:
        if is_prime(factor):
            return factor

if __name__ == '__main__':
    assert is_prime(1) is True
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(9) is False
    assert is_prime(49) is False
    assert largest_prime_factor(13195) == 29

    result = largest_prime_factor(600851475143)
    print 'Result: %d' % result
    assert result == 6857

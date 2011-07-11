from problem_003 import is_prime

def get_prime_by_position(position):
    current_position = 0
    number = 0
    prime = 0

    while current_position <= position:
        number += 1
        if is_prime(number):
            current_position += 1
            prime = number

    return prime

assert get_prime_by_position(6) == 13

result = get_prime_by_position(10001)
print 'Result: %d' % result

assert result == 104743

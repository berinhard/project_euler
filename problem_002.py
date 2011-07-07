def fibonacci_by_limit(fibonacci_limit):
    fibonacci = [0, 1]

    while fibonacci[-2] + fibonacci[-1] < fibonacci_limit:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])

    return fibonacci

def sum_even_numbers(numbers):
    return sum(n for n in numbers if n % 2)

assert fibonacci_by_limit(90) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
assert sum_even_numbers(fibonacci_by_limit(90)) == 188

print 'Result: %d' % sum_even_numbers(fibonacci_by_limit(4 * 10 ** 6))

def sum_of_squares(numbers):
    return sum(n**2 for n in numbers)

def square_of_the_sum(numbers):
    return sum(numbers) ** 2

numbers = range(1, 11)
assert square_of_the_sum(numbers) - sum_of_squares(numbers) == 2640

numbers = range(1, 101)
result = square_of_the_sum(numbers) - sum_of_squares(numbers)

print 'Result: %d' % result
assert result == 25164150

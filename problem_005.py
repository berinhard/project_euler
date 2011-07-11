def min_divisible_by_range(factors, step=1, initial_value=1):
    number = initial_value

    founded = False
    while not founded:
        number += step

        for factor in factors:
            if number % factor:
                break
        else:
            founded = True

    return number


assert min_divisible_by_range(factors=range(1, 11), step=10, initial_value=10) == 2520

result = min_divisible_by_range(factors=range(1, 21), step=20, initial_value=20)
print 'Result: %d' % result

assert result == 232792560

def is_palindrome(number):
    str_format = str(number)

    for i in xrange(len(str_format) - 1):
        if str_format[i] != str_format[-1 + i * (-1)]:
            return False

    return True

result = max(i * j for i in xrange(100, 1000) for j in xrange(100, 1000) if is_palindrome(i * j))

assert is_palindrome(1) is True
assert is_palindrome(99) is True
assert is_palindrome(989) is True
assert is_palindrome(69896) is True
assert is_palindrome(19) is False
assert is_palindrome(189) is False
assert is_palindrome(12891) is False

print 'Result: %d' % result
assert result == 906609

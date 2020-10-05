import pytest

"""
Give the nth entry in the fibonacci series
                    submitted by abxsantos
"""

def iterative_fibonacci(number):
    """Iterative solution for the fibonacci sequence"""
    fib_array = [0, 1]
    i = 2
    while i <= number:
        last_value = fib_array[-1]
        prev_from_last_value = fib_array[-2]
        fib_array.append(last_value + prev_from_last_value)
        i += 1
    return fib_array[number]


def recursive_fibonacci(number):
    """Recursive solution for the fibonacci sequence"""
    if number < 2:
        return number
    return recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2)


def memoize(function):
    """
    Memoization function used to improve the
    performance of the recursive fibonacci
    sequence function placing each recursive
    call into the cache.

    Use the memoize function for bonus points during the interview
    memoized_fibonacci = memoize(recursive_fibonacci)
    value = memoized_fibonacci(6)
    print(value)
    """
    cache = {}

    def memoized_function(*args):
        if args in cache:
            return cache[args]
        result = function(*args)
        cache[args] = result
        return result

    return memoized_function


class TestFibonacci(object):

    @pytest.mark.parametrize('given_index, expected_result', [
        (0, 0), (1, 1), (5, 5), (6, 8)
    ])
    def test_iterative_fibonacci(self, given_index, expected_result):
        assert iterative_fibonacci(given_index) == expected_result

    @pytest.mark.parametrize('given_index, expected_result', [
        (0, 0), (1, 1), (5, 5), (6, 8)
    ])
    def test_recursive_fibonacci(self, given_index, expected_result):
        assert recursive_fibonacci(given_index) == expected_result

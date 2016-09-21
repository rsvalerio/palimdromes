__author__ = 'rsvalerio'

import numpy


def is_palindrome(number, base):
    num = numpy.base_repr(number, base)
    return num == num[::-1]


def show_smallest_base():
    smallest = []

    for num in range(0, 10000):

        for base in range(2, 36):

            if is_palindrome(num, base):
                smallest.append([num, base])
                break

        if len(smallest) == 1000:
            break

    return smallest

if __name__ == "__main__":
    numbers = show_smallest_base();
    for number in numbers:
        print 'Number: \t\t\t' + repr(number[0])
        print 'Smallest Base Palindrome: \t' + repr(number[1])
        print '--------'

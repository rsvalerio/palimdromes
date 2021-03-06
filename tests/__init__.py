#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of palindromes.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Rodrigo Valerio <rsvalerio@gmail.com>

from preggy import expect

from palindromes import palindrome
from tests.base import TestCase


class PalindromeTestCase(TestCase):
    def test_is_palindrome(self):
        expect(palindrome.is_palindrome(0, 2)).to_equal(True)
        expect(palindrome.is_palindrome(1, 2)).to_equal(True)
        expect(palindrome.is_palindrome(2, 2)).to_equal(False)
        expect(palindrome.is_palindrome(2, 3)).to_equal(True)

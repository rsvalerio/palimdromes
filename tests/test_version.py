#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of palindromes.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Rodrigo Valerio <rsvalerio@gmail.com>

from preggy import expect

from palindromes import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')

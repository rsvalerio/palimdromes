#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of palindromes.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Rodrigo Valerio <rsvalerio@gmail.com>

from setuptools import setup, find_packages
from palindromes import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

requires = [
    'numpy'
]

setup(
    name='palindromes',
    version=__version__,
    description='palimdrome smallest base',
    long_description='''
palimdrome smallest base
''',
    keywords='',
    author='Rodrigo Valerio',
    author_email='rsvalerio@gmail.com',
    url='https://github.com/rsvalerio/palimdrome',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=requires,
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'palindromes=palindromes.cli:main',
        ],
    },
)

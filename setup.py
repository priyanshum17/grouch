#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/grouch.svg
        :target: https://pypi.python.org/pypi/grouch
.. image:: https://img.shields.io/travis/priyanshum17/grouch.svg
        :target: https://travis-ci.org/priyanshum17/grouch

Python Boilerplate contains all the boilerplate you need to create a Python package.


Links:
---------
* `Github <https://github.com/priyanshum17/grouch>`_
"""

from setuptools import setup, find_packages

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Priyanshu Mehta",
    author_email='pmehta305@gatech.edu',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='grouch',
    name='grouch',
    packages=find_packages(include=['grouch']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/priyanshum17/grouch',
    version='0.1.0',
    zip_safe=False,
)

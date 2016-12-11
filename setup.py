#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import kuvalda

setup(
    name="kuvalda",
    version=kuvalda.__version__,
    description="""Damn Simple Validation Kit.""",
    long_description=open("README.rst").read(),
    author="Roma Sokolov",
    author_email="sokolov.r.v@gmail.com",
    url="https://github.com/little-arhat/kuvalda",
    packages=[
        "kuvalda"
    ],
    license="MIT",
    classifiers=(
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ),
)

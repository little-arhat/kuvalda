Kuvalda -- Damn Simple Validation Kit
=====================================

About
-----

Validate dict-like object against schema, using just callables.

Features
--------

- Allows validating and sanitizing dicts using any callables
- Provides several useful helpers
- Easy to use -- no class-based boilerplate!

API
---

``validate`` function takes any mapping as data and another mapping as scheme and check data against scheme. It returns list of errors.

``sanitize`` function takes any mapping as data and another mapping as scheme and converts data according to schema definition.

For more info -- see tests.

Install
-------

~/yourvirtualenv/python setup.py install

pip install kuvalda

License
-------

The MIT License, in LICENSE file.

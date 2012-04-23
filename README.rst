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

Examples
--------

Several schemes:

::

    schema = {
        'key1': str,
        'key2': int,
        'key3': int,
    }

    schema1 = {
        'key1': kuvalda.list_of(int),
        'key2': kuvalda.list_of(kuvalda.list_of(int))
    }

    schema2 = {
       'section1': {
           'key1': str,
           'key2': int
        },
        'section2': kuvalda.mapping(str, int),
        'key1': kuvalda.kind_of(bool)
    }

    schema3 = {
        'key1': int,
        'key2': kuvalda.default('oh, my'),
        'key3': kuvalda.optional(int),
        'key4': kuvalda.optional(kuvalda.list_of(int)),
        'key5': kuvalda.compose(kuvalda.default(42), int)
    }


Install
-------

~/yourvirtualenv/python setup.py install

pip install kuvalda

License
-------

The MIT License, in LICENSE file.

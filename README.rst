Kuvalda -- Damn Simple Validation Kit
=====================================

About
-----

Validate dict-like object against schema, using just callables.

Features
--------

- Knows str, int, list, boolean and None types
- Supports sections and subsections
- Easy to use -- one function!

API
---

``parse`` function takes any iterable (file object, for example), which produces strings and returns filled ``dict`` or raises ``ParseError``

FAQ
---

Q1: Does 'dosca' have validation capabilities?

A1: No, it's not. If you want validate your config, use library designed for this task.
`Contract <https://github.com/barbuza/contract>`_, `Procrustes <https://github.com/Deepwalker/procrustes>`_ or, perhaps, Damn Simple Validation Library?



Q2: Does it support interpolation or some complex types?

A2: No, it's not. When I say 'simple', I mean really simple. Dosca only support basic things, essential for parsing config files.
If you want advanced features, use `ConfigObj <http://www.voidspace.org.uk/python/configobj.html>`_ or `ConfigParser <http://docs.python.org/library/configparser.html>`_. Or xml and dtd?

Install
-------

~/yourvirtualenv/python setup.py install

pip install dosca

License
-------

The MIT License, in LICENSE file.

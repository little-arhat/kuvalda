#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import kuvalda


class KuvaldaSuite(unittest.TestCase):
    def test_simple_types_good(self):
        data = {
            'key1': 'string',
            'key2': '41',
            'key3': [1, '2', 3]
        }
        schema = {
            'key1': str,
            'key2': int,
            'key3': list,
        }
        result = {
            'key1': 'string',
            'key2': 41,
            'key3': [1, '2', 3]
        }
        self.assertEqual(kuvalda.sanitize(data, schema), result)

    def test_simple_types_bad(self):
        bad_data = {
            'key1': 'string',
            'key2': 'EVIL',
            'key3': []
        }
        schema = {
            'key1': str,
            'key2': int,
            'key3': int,
        }

        self.assertRaises(kuvalda.ValidationError, kuvalda.sanitize,
                          bad_data, schema)

    def test_composite_types(self):
        data = {
            'key1': [1, '2'],
            'key2': [[1], ['2']]
        }
        bad_data = {
            'key1': [1, ['EVIL']],
            'key2': [[1], ['EVIL']]
        }
        schema = {
            'key1': kuvalda.list_of(int),
            'key2': kuvalda.list_of(kuvalda.list_of(int))
        }
        result = {
            'key1': [1, 2],
            'key2': [[1], [2]]
        }
        self.assertEqual(kuvalda.sanitize(data, schema), result)
        self.assertRaises(kuvalda.ValidationError, kuvalda.sanitize,
                          bad_data, schema)

    def test_mappings_and_sections(self):
        data = {
            'section1': {
                'key1': 'str',
                'key2': 42,
                },
            'section2': {
                'key1': 1,
                'key2': 2,
                'key3': 3
                },
            'key1': True
        }
        bad_data = {
            'section1': {
                'key1': '',
                'key2': 'EVIL',
                },
            'section2': {
                'key1': 'EVIL',
                2: 'key2',
                3: 3,
                },
            'key1': False
        }
        schema = {
            'section1': {
                'key1': str,
                'key2': int
             },
             'section2': kuvalda.mapping(str, int),
             'key1': kuvalda.kind_of(bool)
        }

        self.assertEqual(kuvalda.validate(data, schema), [])
        errors = kuvalda.validate(bad_data, schema)
        self.assertNotEqual(errors, [])
        for error in errors:
            self.assertRaises(kuvalda.ValidationError, self._raise, error)

    def test_default_and_optional(self):
        data = {
            'key1': 42,
            'key4': ['42'],
            'key5': '1'
        }
        schema = {
            'key1': int,
            'key2': kuvalda.default('oh, my'),
            'key3': kuvalda.optional(int),
            'key4': kuvalda.optional(kuvalda.list_of(int)),
            'key5': kuvalda.compose(kuvalda.default(42), int)
        }
        result = {
            'key1': 42,
            'key2': 'oh, my',
            'key3': None,
            'key4': [42],
            'key5': 1
            }
        self.assertEqual(kuvalda.sanitize(data, schema), result)

    def _raise(self, exc):
        raise exc


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-

import sys
import copy

from functools import wraps, partial


class ValidationError(ValueError, TypeError):
    def __init__(self, key, exc):
        msg = 'Key `{0}` has error: {1}'.format(key, exc)
        self.key = key
        self.exception = exc
        super(self.__class__, self).__init__(msg)


def sanitize(data, schema):
    data = copy.deepcopy(data)
    sanitize_in_place(data, schema)
    return data


def sanitize_in_place(data, schema, prefix=None):
    current_key = None
    try:
        for (key, value_spec) in yield_pairs(schema):
            current_key = key
            value = data.get(key)
            # don't use EAFP here, cause we can catch too many exceptions
            if hasattr(value_spec, '__call__'):
                data[key] = value_spec(value)
            else:
                sanitize_in_place(data[key], value_spec, join(prefix, key))
    except (TypeError, ValueError):
        exception = sys.exc_info()[1]
        raise ValidationError(join(prefix, current_key), exception)


def validate(data, schema, prefix=None):
    errors = []
    for (key, value_spec) in yield_pairs(schema):
        value = data.get(key)
        if hasattr(value_spec, '__call__'):
            try:
                answ = value_spec(value)
                if answ is False:
                    raise ValueError('{0} returns False'.format(value_spec))
            except (TypeError, ValueError):
                exception = sys.exc_info()[1]
                errors.append(ValidationError(join(prefix, key), exception))
        else:
            validate(data[key], value_spec, join(prefix, key))
    return errors


def compose(*funcs):
    @wraps(compose)
    def inner(candidate):
        return reduce(lambda acc, f: f(acc), funcs, candidate)
    return inner


def map_(func):
    return partial(map, func)


def list_of(func):
    return compose(list, map_(func))


def yield_pairs(it):
    try:
        return it.iteritems()
    except AttributeError:
        return iter(it)


def mapping(key_func, value_func):
    @wraps(mapping)
    def inner(candidate):
        res = {}
        for (key, value) in yield_pairs(candidate):
            res[key_func(key)] = value_func(value)
        return res
    return inner


def default(default_value):
    @wraps(default)
    def inner(value):
        if value is None:
            return default_value
        else:
            return value
    return inner


def optional(*funcs):
    @wraps(optional)
    def inner(value):
        if value is None:
            return None
        else:
            return compose(*funcs)(value)
    return inner


def join(prefix, key):
    if prefix is None:
        return key
    else:
        return '{0}/{1}'.format(prefix, key)


def kind_of(class_or_type_or_tuple):
    @wraps(isinstance)
    def inner(value):
        return isinstance(value, class_or_type_or_tuple)
    return inner

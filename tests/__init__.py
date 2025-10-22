from __future__ import absolute_import, unicode_literals

from mopidy import compat
from mopidy.compat import pathlib


def path_to_data_dir(name):
    path = pathlib.Path(__file__).parent / 'data' / name
    return path.resolve()


class IsA(object):

    def __init__(self, klass):
        self.klass = klass

    def __eq__(self, rhs):
        try:
            return isinstance(rhs, self.klass)
        except TypeError:
            return type(rhs) == type(self.klass)  # noqa

    def __ne__(self, rhs):
        return not self.__eq__(rhs)

    def __repr__(self):
        return str(self.klass)


any_int = IsA(compat.integer_types)
any_str = IsA(compat.string_types)
any_unicode = IsA(compat.text_type)

import size_converter_error as sc_error
import re

STABDARD_NAME_DELIMITERS = '/|;|,'

class Standard:
    def __init__(self, name, items):
        self._name = re.split(STABDARD_NAME_DELIMITERS, name)
        self._items = []
        for i in items:
            self._items.append(str(i))

    def is_match(self, name):
        for item in self._name:
            if item.lower() == name.lower():
                return True
            abbr = re.sub('\(.*\)' , '', item)
            if abbr.lower() == name.lower():
                return True
        return False

    def get_size_index(self, size):
        for index, item in enumerate(self._items):
            if item.lower() == size.lower():
                return index
        raise sc_error.SizeConverterUnsupportedSizeError(self._name, size)

    def get_size_name(self, index):
        try:
            return self._items[index]
        except IndexError:
            raise sc_error.SizeConverterUnsupportedSizeIndexError(self._name, index)

class Standards:
    def __init__(self, category, items):
        self._category = category
        self._standards = []
        for s in items:
            name = s[0]
            std = Standard(name, s[1:])
            self._standards.append(std)

    def is_match(self, category):
        return sorted(self._category) == sorted(category)

    def get_size_index(self, standard_name, size):
        for s in self._standards:
            if s.is_match(standard_name):
                return s.get_size_index(size)
        raise sc_error.SizeConverterUnsupportedStandardError(standard_name)

    def get_size_name(self, standard_name, index):
        for s in self._standards:
            if s.is_match(standard_name):
                return s.get_size_name(index)
        raise sc_error.SizeConverterUnsupportedStandardError(standard_name)

    def convert_size(self, from_standand, to_standard, size):
        index = self.get_size_index(from_standand, size)
        return self.get_size_name(to_standard, index)

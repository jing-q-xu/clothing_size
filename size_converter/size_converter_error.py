
class SizeConverterError(Exception):
    def __init__(self, info = "unsupported size conversion"):
        self._error_info = info

    def __str__(self):
        return repr(self._error_info)


class SizeConverterUnsupportedSizeError(SizeConverterError):
    def __init__(self, standard, size):
        self._standard = standard
        self._size = size

    def __str__(self):
        return repr('standard %s has no %s value' %(self._standard, self._size))


class SizeConverterUnsupportedSizeIndexError(SizeConverterError):
    def __init__(self, standard, size):
        self._standard = standard
        self._size = size

    def __str__(self):
        return repr('standard %s has no value with index %s' %(self._standard, self._size))


class SizeConverterUnsupportedStandardError(SizeConverterError):
    def __init__(self, standard):
        self._standard = standard

    def __str__(self):
        return repr('standard %s not supported' %(self._standard))

class SizeConverterUnsupportedCategoryError(SizeConverterError):
    def __init__(self, category):
        self._category = category

    def __str__(self):
        return repr('unsupported category [%s]' %(self._category.__str__()))
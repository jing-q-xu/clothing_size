import size_converter_error as sc_error
import re
import standards

CATEGORY_DELIMITERS = '/| |;|,'

class SizeRepo:
    def __init__(self):
        self._size_repo = []
            
    def convert_size(self, category, from_standand, to_standard, size):
        for stds in self._size_repo:
            if stds.is_match(category):
                return stds.convert_size(from_standand, to_standard, size)
        raise sc_error.SizeConverterUnsupportedCategoryError(category)

    def add_standards(self, category, standard_list):
        self._size_repo.append(standards.Standards(category, standard_list))

repo = SizeRepo()

def convert_size(category, from_standand, to_standard, size):
    return repo.convert_size(re.split(CATEGORY_DELIMITERS, category), from_standand, to_standard, size)

def add_size_standards(category, standard_list):
    return repo.add_standards(category, standard_list)

import csv
import codecs
import re
import os
from converter import add_size_standards

FILE_NAME_DELIMITERS = '_|-'

def _get_category(file_name):
    base = os.path.basename(file_name)
    name = os.path.splitext(base)[0]
    return re.split(FILE_NAME_DELIMITERS, name)


def _load_standards(file_name):
    with codecs.open(file_name, 'rU', encoding='utf-8-sig') as file:
        cfg = csv.reader(file, delimiter=",")
        standards = []
        for row in cfg:
            standards.append(row)
        add_size_standards(_get_category(file_name), standards)


def _load_config_files(path_name):
    for f in os.listdir(path_name):
        if f.endswith(".csv"):
            file = os.path.join(path_name, f)
            _load_standards(file)

def load_config_files():
    _load_config_files('../data')


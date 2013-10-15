"""
    Utils to read intermixed fixed width records files
"""

import os
import gzip

def line_generator(file_name, encoding=None):
    """
        Opens a text file, compressed or not, and return a generator of lines.
    """
    #chech file exists
    if not os.path.exists(file_name):
        raise FileNotFoundError
    #check file type:
    root, ext = os.path.splitext(file_name)
    ext.lower()
    #gzip file
    if ext == '.gz':
        with gzip.open(file_name, mode='rt', encoding=encoding) as f:
            for line in f:
                yield line

    #bz2 file
    elif ext == '.bz2':
        raise NotImplementedError

    #zip file
    elif ext == '.zip':
        raise NotImplementedError

    #assume not compressed, just a text file
    else:
        with open(file_name, mode='rt', encoding=encoding) as f:
            for line in f:
                yield line


def tuple_record_generator(record_def, line_iterable):
    """
        Returns a generator of tuples of fields according to the records definition object

        - record_def: Record definition object that comply to the api is_record and to_tuple
        - line_iterable: Collection of text lines representing records
    """

    for line in line_iterable:
        if record_def.is_record(line):
            yield record_def.to_tuple(line)


def dict_record_generator(record_def, line_iterable):
    """
        Returns a generator of dicts of fields according to the records definition object

        - record_def: Record definition object that comply to the api is_record and to_tuple
        - line_iterable: Collection of text lines representing records
    """

    for line in line_iterable:
        if record_def.is_record(line):
            yield record_def.to_dict(line)
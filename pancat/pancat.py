"""
    Utilidades para cargar ficheros de intercambio .cat del Catastro.
"""

import numpy as np
import pandas as pd
from pancat.fincat import FinCat
from pancat.ifwf import line_generator, tuple_record_generator

def read_cat_as_dataframe(fichero_cat, tipo_registro, columns=None):
    """
        Devuelve un pandas.DataFrame con los registros del el tipo deseado

        - fichero_cat: fichero .cat, puede estar comprimido.
        - tipo_registro: Tipo de registro, p.ej.: '11', '15'
        - columns: Lista con los nombres de los campos que se quiere cargar.
    """
    reg_def = FinCat(tipo_registro, columns)
    cat_gen = line_generator(fichero_cat, encoding='latin1')
    return pd.DataFrame.from_records(list(tuple_record_generator(reg_def, cat_gen)), columns=reg_def.columns)

def read_cat_as_ndframe(fichero_cat, tipo_registro, columns=None):
    """
        Devuelve un numpy.ndframe con los registros del el tipo deseado

        - fichero_cat: fichero .cat, puede estar comprimido.
        - tipo_registro: Tipo de registro, p.ej.: '11', '15'
        - columns: Lista con los nombres de los campos que se quiere cargar.
    """
    reg_def = FinCat(tipo_registro, columns)

    # count number of registers. Two pass strategy.
    count=0
    count_gen = line_generator(fichero_cat, encoding='latin1')
    for reg in count_gen:
        if reg_def.is_record(reg):
            count += 1

    line_gen = line_generator(fichero_cat, encoding='latin1')
    cat_gen = tuple_record_generator(reg_def, line_gen)
    dtypes = list(zip(reg_def.columns, reg_def.dtypes))
    ndarray = np.empty(count, dtype=dtypes, order='F')
    nrec = 0
    while(nrec < count):
        try:
            record = next(cat_gen)
        except(StopIteration):
            #check if iterator exhausted before reach count and downsize array
            ndarray.resize(nrec)
            break;
        ndarray[nrec] = record
        nrec += 1
    return ndarray


"""
Fichero donde se define la estructura de los registros del fichero de intercambio

Ver: http://www.catastro.minhap.es/ayuda/lang/castellano/ayuda_descarga_cat.htm
"""

from functools import partial

# funciones para procesar los campos.

def codigo(campo):
    """
    Procesa un campo de tipo código. Carácteres alfanuméricos, sin recorte de espacios.
    """
    return campo if not campo.isspace() else ''

def texto(campo):
    """
    Procesa un campo de tipo texto, recorta espacios por la derecha.
    """
    return campo.rstrip()

def numero_decimal(campo, parte_entera=3):
    """
    Procesa un campo que representa un número decimal.
    parte_entera son los carácteres a la derecha correpondientes a
    la parte entera del número decimal
    """
    return float('.'.join((campo[:parte_entera], campo[parte_entera:]))) if not None else ''

def numero_entero(campo):
    """
    Procesa un campo que representa un número entero
    """
    return int(campo) if not None else ''

def fecha(campo):
    """
    Procesa un campo que representa una fecha en YYYYMMDD
    y lo pasa como un string YYYY-MM-DD
    """
    return '-'.join((campo[:4], campo[4:6], campo[6:])) if not campo.isspace() else ''

def hora(campo):
    """
    Procesa un campo que representa una hora en HHMMSS
    y lo devuelve como un string HH:MM:SS
    """
    return ':'.join((campo[:2], campo[2:4], campo[4:])) if not campo.isspace() else ''

def fecha_hora(campo):
    """
    Procesa un campo que representa una fecha y hora en YYYYMMDDHHMMSS
    y lo pasa como un string YYYY-MM-DD HH:MM:SS
    """
    f = '-'.join((campo[:4], campo[4:6], campo[6:]))
    h = ':'.join((campo[:2], campo[2:4], campo[4:]))
    return ' '.join(f, h) if not campo.isspace() else ''

# definición de los registros

registro_de_cabecera = {
    # tipo de registro
    'tipo_registro': (1, 2, codigo, 'U2'),
    # identificación de la entidad generadora
    'tipo_entidad_generadora': (3, 1, codigo, 'U1'),
    'codigo_entidad_generadora': (4, 9, codigo, 'U9'),
    'nombre_entidad_generadora': (13, 27, texto, 'U27'),
    # datos del fichero
    'fecha_hora_generacion': (40, 14, fecha_hora, 'U19'),
    'tipo_fichero': (54, 4, texto, 'U4'),
    'descripcion_fichero': (58, 39, texto, 'U39'),
    'nombre_fichero': (97, 21, texto, 'U21'),
    'codigo_entidad_destinataria': (118, 3, codigo, 'U3'),
    # datos específicos del formato
    'fecha_inicio_periodo': (121, 8, fecha, 'U10'),
    'fecha_fin_periodo': (129, 8, fecha, 'U10'),
    }

registro_de_finca = {
    # tipo de registro 11
    'tipo_registro': (1, 2, codigo, 'U2'),
    # identificación de la parcela catastral
    'codigo_delegacion_meh': (24, 2, codigo, 'U2'),
    'codigo_municipio_dgc': (26, 3, codigo, 'U3'),
    'parcela_catastral': (31, 14, codigo, 'U14'),
    # domicilio tributario / localizacion de la parcela
    'codigo_provincia': (51, 2, codigo, 'U2'),
    'nombre_provincia': (53, 25, texto, 'U25'),
    'codigo_municipio_dgc': (78, 3, codigo, 'U3'),
    'codigo_municipio_ine': (81, 3, codigo, 'U3'),
    'nombre_municipio': (84, 40, texto, 'U40'),
    'nombre_entidad_menor': (124, 30, texto, 'U30'),
    'codigo_via_dgc': (154, 5, codigo, 'U5'),
    'tipo_via': (159, 5, codigo, 'U5'),
    'nombre_via': (164, 25, texto, 'U25'),
    'numero': (189, 4, numero_entero, 'i4'),
    'letra': (193, 1, codigo, 'U1'),
    'numero2': (194, 4, numero_entero, 'i4'),
    'letra2': (198, 1, codigo, 'U1'),
    'kilometro': (199, 5, partial(numero_decimal, parte_entera = 3), 'f4'),
    'bloque': (204, 4, codigo, 'U4'),
    'texto_direccion': (216, 25, texto, 'U25'),
    'codigo_postal': (241, 5, codigo, 'U5'),
    'distrito_municipal': (246, 2, codigo, 'U2'),
    'codigo_municipio_origen_agregacion': (248, 3, codigo, 'U3'),
    'zona_concentracion': (251, 2, codigo, 'U2'),
    'poligono': (253, 3, codigo, 'U3'),
    'parcela': (256, 5, codigo, 'U5'),
    'codigo_paraje': (261, 5, codigo, 'U5'),
    'nombre_paraje': (266, 30, texto, 'U30'),
    # datos físicos
    'superficie_parcela': (296, 10, numero_entero, 'U8'),
    'superficie_construida': (306, 7, numero_entero, 'U8'),
    'superficie_construida_sobre_rasante': (313, 7, numero_entero, 'U8'),
    'superficie_construida_bajo_rasante': (320, 7, numero_entero, 'U8'),
    'superficie_cubierta': (327, 7, numero_entero, 'U8'),
    # coordenadas de la finca
    'coordenada_x': (334, 9, partial(numero_decimal, parte_entera = 7), 'f8'),
    'coordenada_y': (343, 10, partial(numero_decimal, parte_entera = 8), 'f8'),
    'srs': (667, 10, texto, 'U10'),
    # referencia bice
    'rc_bice': (582, 20, codigo, 'U20'),
    'denominacion_bice': (602, 65, texto, 'U65'),
    }

registro_de_unidad_constructiva = {
    # tipo de registro 13
    'tipo_registro': (1, 2, codigo, 'U2'),
    # identificación de la parcela catastral
    'codigo_delegacion_meh': (24, 2, codigo, 'U2'),
    'codigo_municipio_dgc': (26, 3, codigo, 'U3'),
    'clase_unidad_constructiva': (29, 2, codigo, 'U2'),
    'parcela_catastral': (31, 14, codigo, 'U14'),
    'codigo_unidad_constructiva': (45, 4, codigo, 'U4'),
    # domicilio tributario / localizacion de la parcela
    'codigo_provincia': (51, 2, codigo, 'U2'),
    'nombre_provincia': (53, 25, texto, 'U25'),
    'codigo_municipio_dgc': (78, 3, codigo, 'U3'),
    'codigo_municipio_ine': (81, 3, codigo, 'U3'),
    'nombre_municipio': (84, 40, texto, 'U40'),
    'nombre_entidad_menor': (124, 30, texto, 'U30'),
    'codigo_via_dgc': (154, 5, codigo, 'U5'),
    'tipo_via': (159, 5, codigo, 'U5'),
    'nombre_via': (164, 25, texto, 'U25'),
    'numero': (189, 4, numero_entero, 'i4'),
    'letra': (193, 1, codigo, 'U1'),
    'numero2': (194, 4, numero_entero, 'i4'),
    'letra2': (198, 1, codigo, 'U1'),
    'kilometro': (199, 5, partial(numero_decimal, parte_entera = 3), 'f4'),
    'texto_direccion': (216, 25, texto, 'U25'),
    # datos fisicos
    'año_construccion': (296, 4, codigo, 'U4'),
    'indicador_exactitud_año_construccion': (300, 1, codigo, 'U1'),
    'superficie_suelo_ocupada': (301, 7, numero_entero, 'U8'),
    'longitud_fachada': (308, 5, numero_entero, 'U4'),
    'codigo_unidad_constructiva_matriz': (410, 4, codigo, 'U4'),
    }

registro_de_construccion = {
    # tipo de registro 14
    'tipo_registro': (1, 2, codigo, 'U2'),
    # identificación de la parcela catastral
    'codigo_delegacion_meh': (24, 2, codigo, 'U2'),
    'codigo_municipio_dgc': (26, 3, codigo, 'U3'),
    'parcela_catastral': (31, 14, codigo, 'U14'),
    'numero_orden_construccion': (45, 4, codigo, 'U4'),
    # informacion adicional
    'numero_cargo': (51, 4, codigo, 'U4'),
    'codigo_unidad_constructiva': (55, 4, codigo, 'U4'),
    # domicilio tributario / localizacion interior
    'bloque': (59, 4, codigo, 'U4'),
    'escalera': (63, 2, codigo, 'U2'),
    'planta': (65, 3, codigo, 'U3'),
    'puerta': (68, 3, codigo, 'U3'),
    #datos fisicos
    'codigo_destino_dgc': (71, 3, codigo, 'U3'),
    'indicador_reforma': (74, 1, codigo, 'U1'),
    'año_reforma': (75, 4, numero_entero, 'U4'),
    'año_antiguedad_efectiva_catastro': (79, 4, numero_entero, 'U4'),
    'indicador_local_interior': (83, 1, codigo, 'U1'),
    'superficie_total_local_catastro': (84, 7, numero_entero, 'U8'),
    'superficie_porches_terrazas': (91, 7, numero_entero, 'U8'),
    'superficie_otras_plantas': (98, 7, numero_entero, 'U8'),
    'tipologia_constructiva': (105, 5, codigo, 'U5'),
    'codigo_modalidad_reparto': (112, 3, codigo, 'U3'),
    }

registro_de_bien_inmueble = {
    # tipo de registro 15
    'tipo_registro': (1, 2, codigo, 'U2'),
    # identificación del bien inmueble
    'codigo_delegacion_meh': (24, 2, codigo, 'U2'),
    'codigo_municipio_dgc': (26, 3, codigo, 'U3'),
    'clase_bien_inmueble': (29, 2, codigo, 'U2'),
    'parcela_catastral': (31, 14, codigo, 'U14'),
    'numero_cargo': (45, 4, codigo, 'U4'),
    'caracter_control_1': (49, 1, codigo, 'U1'),
    'caracter_control_2': (50, 1, codigo, 'U1'),
    #identificadores adicionales
    'identificacion_dgc': (51, 8, codigo, 'U8'),
    'identificacion_ayuntamiento': (59, 15, codigo, 'U15'),
    'identificacion_registral': (74, 19, codigo, 'U19'),
    # domicilio tributario / localizacion del bien inmueble
    'codigo_provincia': (93, 2, codigo, 'U2'),
    'nombre_provincia': (95, 25, texto, 'U25'),
    'codigo_municipio_dgc': (120, 3, codigo, 'U3'),
    'codigo_municipio_ine': (123, 3, codigo, 'U3'),
    'nombre_municipio': (126, 40, texto, 'U40'),
    'nombre_entidad_menor': (166, 30, texto, 'U30'),
    'codigo_via_dgc': (196, 5, codigo, 'U5'),
    'tipo_via': (201, 5, codigo, 'U5'),
    'nombre_via': (206, 25, texto, 'U25'),
    'numero': (231, 4, numero_entero, 'i4'),
    'letra': (235, 1, codigo, 'U2'),
    'numero2': (236, 4, numero_entero, 'i4'),
    'letra2': (240, 1, codigo, 'U1'),
    'kilometro': (241, 5, partial(numero_decimal, parte_entera = 3), 'f4'),
    'bloque': (246, 4, codigo, 'U4'),
    'escalera': (250, 2, codigo, 'U2'),
    'planta': (252, 3, codigo, 'U3'),
    'puerta': (255, 3, codigo, 'U3'),
    'texto_direccion': (258, 25, texto, 'U25'),
    'codigo_postal': (283, 5, codigo, 'U5'),
    'distrito_municipal': (288, 2, codigo, 'U2'),
    'codigo_municipio_origen_agregacion': (290, 3, codigo, 'U3'),
    'zona_concentracion': (293, 2, codigo, 'U2'),
    'poligono': (295, 3, codigo, 'U3'),
    'parcela': (298, 5, codigo, 'U5'),
    'codigo_paraje': (303, 5, codigo, 'U5'),
    'nombre_paraje': (308, 30, codigo, 'U30'),
    # informacion adicional
    'numero_orden_escritura_lph': (368, 4, codigo, 'U4'),
    'año_antiguedad': (372, 4, numero_entero, 'i4'),
    # datos economicos del bien inmueble
    'clave_uso': (428, 1, codigo, 'U1'),
    'superficie_construida': (442, 10, numero_entero, 'U8'),
    'superficie_no_construida': (452, 10, numero_entero, 'U8'),
    'coeficiente_propiedad': (462, 9, codigo, 'U9'),
    }

registro_de_reparto_de_elemetos_comunes = {
    # tipo de registro 16
    'tipo_registro': (1, 2, codigo, 'U2'),
    # identificación de la parcela catastral
    'codigo_delegacion_meh': (24, 2, codigo, 'U2'),
    'codigo_municipio_dgc': (26, 3, codigo, 'U3'),
    'parcela_catastral': (31, 14, codigo, 'U14'),
    'numero_orden': (45, 4, codigo, 'U4'),
    'calificacion_catastral': (49, 2, codigo, 'U2'),
    # bloque repetitivo de reparto
    'numero_orden_registro_repartos': (51, 4, codigo, 'U4'),
    'numero_cargo_reparte_elemento_comun': (55, 4, codigo, 'U4'),
    'porcentaje_reparto': (59, 6, partial(numero_decimal, parte_entera = 3), 'f8'),
    # ..... TODO: repeticiones???
    # .....
    }

registro_de_cultivos = {
    # tipo de registro 17
    'tipo_registro': (1, 2, codigo, 'U2'),
    # identificación de la parcela catastral
    'codigo_delegacion_meh': (24, 2, codigo, 'U2'),
    'codigo_municipio_dgc': (26, 3, codigo, 'U3'),
    'naturaleza_suelo': (29, 2, codigo, 'U2'),
    'parcela_catastral': (31, 14, codigo, 'U14'),
    'codigo_subparcela': (45, 4, codigo, 'U4'),
    # informacion adicional
    'numero_cargo': (51, 4, codigo, 'U4'),
    # datos físicos y económicos
    'tipo_subparcela': (55, 1, codigo, 'U1'),
    'superficie_subparcela': (56, 10, numero_entero, 'U8'),
    'clase_cultivo': (66, 2, codigo, 'U2'),
    'denominacion_cultivo': (68, 40, texto, 'U40'),
    'intensidad_productiva': (108, 2, codigo, 'U2'),
    'codigo_modalidad_reparto': (127, 3, codigo, 'U3'),
    }


registros = { '01': registro_de_cabecera,
              '11': registro_de_finca,
              '13': registro_de_unidad_constructiva,
              '14': registro_de_construccion,
              '15': registro_de_bien_inmueble,
              '16': registro_de_reparto_de_elemetos_comunes,
              '17': registro_de_cultivos,
              }

# clase para gestión de registros

class FinCat(object):
    """
        Clase de ayuda para extraer los campos de un registro según su definición.
    """
    def __init__(self, identifier, fields=None):
        """
            Constructor de la calse de gestión de registros

            identifier: Identificador del registro, empieza por. p.ej.: '11', '15'
            fields: Lista con los campos a extraer del registro.
        """
        # set record identifier and record definition dict.
        self.identifier = identifier
        if identifier not in registros:
            raise NotImplementedError('Error, tipo de registro no definido')
        self.record_def_dict = registros[identifier]

        # set columns names
        if fields:
            for field in fields:
                if field not in self.record_def_dict:
                    raise ValueError("El campo %s no se encuentra en la definición del registro") % field
            self.columns = fields
        else: #all fields
            self.columns = self.record_def_dict.keys()

        # numpy dtypes
        self.dtypes=[]
        for field in self.columns:
            self.dtypes.append(self.record_def_dict[field][3])

    def is_record(self, record):
        """
            Comprueba que el registro pasado corresponde al tipo definido.
        """
        return True if record.startswith(self.identifier) else False

    def to_tuple(self, record):
        """
            Convierte un registro a una tupla de campos.
        """
        return tuple(self.to_list(record))

    def to_list(self, record):
        """
            Convierte un registro a una lista de campos.
        """
        fields = []
        if self.is_record(record):
            for name in self.columns:
                start, width, func, _ = self.record_def_dict[name]
                start -= 1
                end = start + width
                fields.append(func(record[start:end]))
        return fields

    def to_dict(self, record):
        """
            Convierte un registro a un diccionario con los campos.
        """
        fields = {}
        if self.is_record(record):
            for name in self.columns:
                start, width, func, _ = self.record_def_dict[name]
                start -= 1
                end = start + width
                fields[name] = func(record[start:end])
        return fields
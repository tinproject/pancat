# pancat: paquete de análisis de ficheros del catastro.

## Qué es

Colección de utilidades para la carga de datos de ficheros de intercambio de la Dirección General del Catastro Española

## Requisitos

 * Python 3
 * pandas

## Cómo usarlo

```python
import pancat as pc

# pandas DataFrame
df = pc.read_cat_as_dataframe('archivo.cat.gz', '15')

#numpy structured ndarray
array = pc.read_cat_as_ndarray('archivo.cat.gz', '15')
```

## A futuro

El objetivo es ir acumulando herramientas para trabajar con los ficheros de datos que proporciona el Catastro de forma sencilla.

Para solicitar nuevas funcionalidades o reportar fallos, por favor, crea una nueva 'issue'.

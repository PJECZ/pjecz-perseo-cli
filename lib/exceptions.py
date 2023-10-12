"""
Lib - Exceptions
"""


class MyAnyError(Exception):
    """Excepcion base para todas las excepciones del My"""


class MyAuthenticationError(MyAnyError):
    """Excepcion porque falla la autenticacion"""


class MyConfigurationError(MyAnyError):
    """Excepcion porque falta algo en la configuracion"""


class MyConnectionError(MyAnyError):
    """Excepcion porque falla la comunicacion o no llega la respuesta"""


class MyFileNotFoundError(MyAnyError):
    """Excepcion porque no existe el archivo"""


class MyNoDataWarning(MyAnyError):
    """Excepcion porque lo que llega no es lo esperado"""


class MyNotValidParamError(MyAnyError):
    """Excepción porque un parámetro es inválido"""


class MyOutOfRangeParamError(MyAnyError):
    """Excepción porque un parámetro esta fuera de rango"""


class MyRequestError(MyAnyError):
    """Excepcion porque falla la comunicacion o no llega la respuesta"""


class MyResponseError(MyAnyError):
    """Excepcion porque lo que llega no es lo esperado"""


class MyStatusCodeError(MyAnyError):
    """Excepcion porque el status code no es 200"""

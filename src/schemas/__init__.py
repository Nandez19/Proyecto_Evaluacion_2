from .autor import AutorCreate, AutorResponse
from .bibliotecario import bibliotecarioCreate, bibliotecarioResponse
from .editorial import editorialCreate, editorialResponse
from .libro import libroCreate, libroResponse
from .prestamo import prestamoCreate, prestamoResponse

__all__ = [
    "AutorCreate",
    "AutorResponse",
    "bibliotecarioCreate",
    "bibliotecarioResponse",
    "editorialCreate",
    "editorialResponse",
    "libroCreate",
    "libroResponse",
    "prestamoCreate",
    "prestamoResponse"
]
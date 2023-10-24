"""
Universal Mixin
"""
from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import func


class UniversalMixin:
    """Columnas y metodos universales"""

    creado = Column(DateTime, default=func.now(), nullable=False)
    modificado = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    estatus = Column(String(1), default="A", nullable=False)


from datetime import date
from unicodedata import numeric
from xmlrpc.client import Boolean

from flask_appbuilder import Model
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Categoria(Model):
    _tablename_ = 'categorias'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique = True, nullable=False)
    descripcion = Column(String(250), nullable=True)
    activo = Column(Boolean, default=True, nullable=False)
    
    ingredientes = relationship(
        "Producto",
        back_populates="categoria"
    )
    
    def __repr__(self):
        return self.name
    
    
    
    
    class ingredientes(Model):
        _tablename_ = 'ingredientes'
        id = Column(Integer, primary_key=True)
        nombre = Column(String(100), unique = True, nullable=False)
        categoria_id = Column(Integer, ForeignKey('categorias.id'), nullable=False)
        cantidad = Column(numeric(10, 2), default=True, nullable=False)
        unidad_medida = Column((50), nullable=False)
        costo_unitario = Column(numeric(10, 2), default=True, nullable=False)
        stock_minimo = Column(numeric(10, 2), default=True, nullable=False)
        fecha_vencimiento = Column(date(50), nullable=False)
        activo = Column(Boolean, default=True, nullable=False)
        
        categoria= relationship(
            "categoria",
            back_populates="ingrediente"
        )
        
        def __repr__(self):
            return self.name
from sqlalchemy import Column, Integer, String
from conexion import Base
class User(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True)
    NombreCompleto = Column(String(20))
    correoElectrico = Column(String(40))
    Contraseña = Column(String(20))
    Direccion = Column(String(100))
    Telefono = Column(Integer)
    Estado = Column(Integer)

class Noticia(Base):
    __tablename__ = "noticias"
    id = Column(Integer, primary_key=True, index=True)
    Titulo = Column(String(50))
    Descripcion = Column(String(10000))

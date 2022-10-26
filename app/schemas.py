from typing import Optional
from pydantic import BaseModel
class User(BaseModel):
    id : Optional[int]
    NombreCompleto: str 
    correoElectrico: str 
    Contraseña: str
    Direccion: str 
    Telefono: int 
    Estado: int 
    #mapeado de los objetps
    class Config:
        orm_mode = True
class ValidarUser(BaseModel):
    correoElectrico: str 
    Contraseña: str
    class Config:
        orm_mode = True

class Noticia(BaseModel):
    id : Optional[int]
    Titulo: str
    Descripcion: str
    class Config:
        orm_mode = True

class NoticiaUpdate(BaseModel):
    Titulo: str
    Descripcion: str
    class Config:
        orm_mode = True

class NoticiaDelete(BaseModel):
    mensaje: str
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    NombreCompleto: str 
    class Config:
        orm_mode = True

class UserDelete(BaseModel):
    mensaje: str
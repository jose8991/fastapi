#importamos las librerias necesarias
from typing import List
from urllib import response
from starlette.responses import RedirectResponse
#base de datos
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import schemas,models
from conexion import SessionLocal, engine
#importamos fast api


models.Base.metadata.create_all(bind=engine)

app=FastAPI()

#creamos una funcion para obtener la sesion
async def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
#creamodor de usuarios

@app.get("/")
def read_users():
    return RedirectResponse(url="/docs")

@app.get("/usuarios/",response_model=List[schemas.User])
def show__users(Session=Depends(get_db)):
    usuarios=Session.query(models.User).all()
    return usuarios

@app.post("/usuario/login",response_model=schemas.User)
def login_user(user:schemas.ValidarUser,Session=Depends(get_db)):
    new_user=models.User(correoElectrico=user.correoElectrico,Contraseña=user.Contraseña)
    print(new_user)
    return new_user


@app.post("/usuarios/",response_model=schemas.User)
def create__users(entrada:schemas.User,Session=Depends(get_db)):
    usuario=models.User(NombreCompleto=entrada.NombreCompleto
    ,correoElectrico=entrada.correoElectrico,Contraseña=entrada.Contraseña,Direccion=entrada.Direccion
    ,Telefono=entrada.Telefono,Estado=entrada.Estado)
    Session.add(usuario)
    Session.commit()
    Session.refresh(usuario)
    return usuario

@app.put("/usuarios/{usuario_id}",response_model=schemas.User)
def update__users(usuario_id:int,entrada:schemas.UserUpdate,Session=Depends(get_db)):
    usuario= Session.query(models.User).filter_by(id=usuario_id).first()
    usuario.NombreCompleto=entrada.NombreCompleto
    Session.commit()
    Session.refresh(usuario)
    return usuario

@app.delete("/usuarios/{usuario_id}",response_model=schemas.UserDelete)
def delete_users(usuario_id:int,entrada:schemas.UserDelete,Session=Depends(get_db)):
    usuario= Session.query(models.User).filter_by(id=usuario_id).first()
    Session.delete(usuario)
    Session.commit()
    respuesta =  schemas.UserDelete(mensaje="Usuario eliminado")
    return respuesta

@app.get("/noticias/",response_model=List[schemas.Noticia])
def show__noticias(Session=Depends(get_db)):
    noticias=Session.query(models.Noticia).all()
    print(noticias)
    return noticias

@app.post("/noticias/",response_model=schemas.Noticia)
def create__noticias(entrada:schemas.Noticia,Session=Depends(get_db)):
    noticia=models.Noticia(Titulo=entrada.Titulo,Descripcion=entrada.Descripcion)
    Session.add(noticia)
    Session.commit()
    Session.refresh(noticia)
    return noticia

@app.put("/noticias/{noticia_id}",response_model=schemas.Noticia)
def update__noticias(noticia_id:int,entrada:schemas.NoticiaUpdate,Session=Depends(get_db)):
    noticia= Session.query(models.Noticia).filter_by(id=noticia_id).first()
    noticia.Titulo=entrada.Titulo
    noticia.Descripcion=entrada.Descripcion
    Session.commit()
    Session.refresh(noticia)
    return noticia

@app.delete("/noticias/{noticia_id}",response_model=schemas.Noticia)
def delete_noticias(noticia_id:int,entrada:schemas.NoticiaDelete,Session=Depends(get_db)):
    noticia= Session.query(models.Noticia).filter_by(id=noticia_id).first()
    Session.delete(noticia)
    Session.commit()
    return "Noticia eliminada"
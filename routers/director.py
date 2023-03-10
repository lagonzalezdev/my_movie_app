from fastapi import APIRouter, Path, Query
from models.director import Director  as DirectorModel
from schemas.director import Director
from service.director import DirectorService

from typing import List
from config.database import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder



director_router = APIRouter()


@director_router.get('/director',tags= ['director'], response_model= List[Director],status_code= 200)
def get_directors() -> Director: 
    db = Session()
    result = DirectorService(db).get_directors()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@director_router.get('/director/{id}', tags=['director'], response_model=Director,status_code=200)
def get_director_by_id(id: int = Path(ge=0,le=2000)) :
        db = Session()
        result = DirectorService(db).get_director_by_id(id)
        if not result:
            return JSONResponse(status_code=400, content={"message":"Not Found director whit that ID"})
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)

@director_router.get('/director/', tags=['director'],response_model=List[Director],status_code=200) 
def get_director_by_fname(fname:str = Query(min_length=1, max_length=20)): 
        db = Session()                                        
        result = db.query(DirectorModel).filter(DirectorModel.fname == fname).all()
        if not result:
            return JSONResponse(status_code=400, content={"message":"Not Found director whit that first name"})
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)

@director_router.post('/director/',tags=['director'],status_code=200,response_model=dict)
def create_director(director:Director)->dict:
        db = Session()
        DirectorService(db).create_director(director)
        return JSONResponse (content={"message":"Director created sucessfully.","status_code":200})
 
@director_router.put('/director/{fname}', tags=['director'])
def update_director(fname:str,director:Director):
        db = Session()
        result = DirectorService(db).get_director(id)
        if not result:
            return JSONResponse(content={"message":"first name director can't be update","status_code":"404"})
        DirectorService(db).update_director(fname,director)
        return JSONResponse(content={"message":"The director name has been updated whit the name:{fname}"})

@director_router.delete('/director/{lname}', tags=['director'])
def delete_director(lname:str):
        db = Session()
        result = DirectorService(db).get_director(id)
        if not result:
            return JSONResponse(content={"message":"Not Found director whit that first name","status_code":"404"})
        return JSONResponse(content={"message":"Director removed sucessfully", "status_code":200})
                            
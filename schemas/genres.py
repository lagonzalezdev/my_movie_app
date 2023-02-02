from pydantic import BaseModel, Field
from typing import Optional

class Genres (BaseModel):
    id: Optional [int] = None
    title:  str = Field (max_lenght=20, min_lenght_=3)

class Config:
    schema_extra ={
        "example":{
            'id': 2,
            'title': 'fantasy', 
        }
    }
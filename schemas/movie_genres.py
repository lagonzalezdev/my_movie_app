from pydantic import BaseModel

class MovieGenres(BaseModel):

    movie_id: int
    gen_id: int

class config:
    schema_extra= {
        "example":{
            'movie_id': 3,
            'gen_id': 5,
        }
    }
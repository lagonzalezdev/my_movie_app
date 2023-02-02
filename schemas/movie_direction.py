from pydantic import BaseModel

class MovieDirection(BaseModel):
    movie_id: int
    dir_id: int

    class Config:
        schema_extra = {
            "example": {
                "movie_id": 2,
                "dir_id": 2,
            }
        }
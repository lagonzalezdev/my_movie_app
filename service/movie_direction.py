from movie_direction import MovieDirector as MovieDirectionModel
from schemas.movie_direction import MovieDirector

class MovieDirectionService():

    def __init__(self,db) -> None:
        self.db = db

def get_movie_direction(self):
        result = self.db.query(MovieDirectionModel).first()
        return result


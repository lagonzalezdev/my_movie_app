from movie_direction import MovieDirector as MovieDirectionModel
from schemas.movie_direction import MovieDirection

class MovieDirectionService():

    def __init__(self,db) -> None:
        self.db = db

def get_movie_direction(self):
        result = self.db.query(MovieDirectionModel).first()
        return result

def create_movie_direction(self, movie_direction:MovieDirection):
        new_movie_direction = MovieDirectionModel(
            movie_id = movie_direction.id,
            dir_id = movie_direction.dir_id,
        )
        self.db.add(new_movie_direction)
        self.db.commit()
        return

def update_movie_direction(self, dir_id:int, data:MovieDirection):
        movie_direction.movie_id = data.id
        movie_direction = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.dir_id).first()
        self.db.commit()
        return

def delete_movie_direction(self, dir_id:int):
        self.db.query(MovieDirectionModel).filter(MovieDirectionModel.dir_id).delete()
        self.db.commit()
        return

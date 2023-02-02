from movie_genres import MovieGenres as MovieGenresModel
from schemas.movie_genres import MovieGenres

class MovieGenresService():

    def __init__(self,db) -> None:
        self.db = db
    
    def get_movies_genres(self):
        result = self.db.query(MovieGenresModel).all()
        return result
    
    def get_movies_genres(self, movie_id:int):
        result = self.db.query(MovieGenresModel).filter(MovieGenresModel.movie_id == movie_id).first()
        return result

    def get_movie_genres_by_gen_id(self, gen_id:int):
        result = self.db.query(MovieGenresModel).filter(MovieGenresModel.gen_id == gen_id).all()
        return result

    def create_movie_genres(self, movie_genres:MovieGenres):
        new_movie_genres = MovieGenresModel(
            movie_id = movie_genres.movie_id,
            gen_id = movie_genres.gen_id,
        )
        self.db.add(new_movie_genres)
        self.db.commit()
        return

    def update_movie_genres (self, movie_id:int, data:MovieGenres):
        movie_genres = self.db.query(MovieGenresModel).filter(MovieGenresModel.movie_id == movie_id).first()
        movie_genres.gen_id = data.gen_id
        self.db.commit()
        return

    def delete_movie_genres (self, movie_id:int):
        self.db.query(MovieGenresModel).filter(MovieGenresModel.movie_id == movie_id).delete
        self.db.delete()
        self.db.commit()
        return    


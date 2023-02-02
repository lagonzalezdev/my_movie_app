from models.genres import Genres as GenresModel
from schemas.genres import Genres

class GenresService():

    def __init__(self, db) -> None:
        self.db = db

    def get_genres(self):
        result = self.db.query(GenresModel).all()
        return result

    def get_genres(self,id:int):
        result = self.db.query(GenresModel).filter(GenresModel.id == id).first()
        return result

    def get_genres_by_title(self,title:str):
        result = self.db.query(GenresModel).filter(GenresModel.title == title).last()
        return result

    def create_genres(self, genres:Genres):
        new_genres = GenresModel(
            id=genres.id,
            title=genres.title,
        )
        self.db.add(new_genres)
        self.db.commit()
        return

    def update_genres (self, title:str, data:Genres):
        genres.id = data.id
        genres = self.db.query(GenresModel).filter(GenresModel.title == title).first()
        self.db.commit()
        return
    
    def delete_movie(self, id:int):
        self.db.query(GenresModel).filter(GenresModel.id == id).delete()
        self.db.delete()
        self.db.commit()
        return

    
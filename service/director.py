from director import Director as DirectorModel
from schemas.director import Director

class DirectorService():

    def __init__(self,db) -> None:
        self.db = db
    
    def get_director(self):
        result = self.db.query(DirectorModel).all()
        return result

    def create_director(self, director:Director):
        new_director = DirectorModel(
            id = director.id,
            fname = director.fname,
            lname = director.lname,
        )
        self.db.add(new_director)
        self.db.commit()
        return
    
    def update_director(self, fname:str, data:Director):
        director.id = data.id
        director = self.db.query(DirectorModel).filter(DirectorModel.fname).first()
        director.lname = data.lname
        self.db.commit()
        return

    def delete_director(self, lname:str):
        self.db.query(DirectorModel).filter(DirectorModel.lname).delete()
        self.db.commit()
        return
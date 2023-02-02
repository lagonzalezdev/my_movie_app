from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class Movie_direction(Base):
    
    ___tablename__="movie_direction"

    movie_id = Column(Integer, ForeignKey("movie.id"))
    dir_id = Column(Integer, ForeignKey("director.id"))

from sqlalchemy import Column, ForeignKey ,Integer, String, Float,Date
from sqlalchemy.orm import relationship

from config.database import Base
from models.actor import Actor

class MovieGenres(Base):

    __tablename__="movie_genres"

    movie_id = Column(Integer, ForeignKey("movie.id"))
    gen_id = Column(Integer, ForeignKey("genres.id"))


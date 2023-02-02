from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from config.database import Base

class Rating (Base):
    
    ___tablename__="rating"
    movie_id = Column(Integer, ForeignKey("movie.id"))
    rev_id = Column(Integer, ForeignKey("reviewer.id"))
    rev_stars = Column(Integer)
    num_o_ratings = Column(Integer)


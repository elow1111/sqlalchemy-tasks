from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie, Director
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def get_movies_with_directors(session):
    stmt = (
        select(Movie, Director)
        .join(Director, Director.id == Movie.director_id)  # Уточняем, как соединяем таблицы
        .order_by(Movie.title)
    )
    
    results = session.execute(stmt).all()
    
    movies_with_directors = [
        f"{movie.title} by {director.name}, released on {movie.release_date}, duration: {movie.duration} min, genre: {movie.genre}, rating: {movie.rating}"
        for movie, director in results
    ]
    
    return movies_with_directors
# END

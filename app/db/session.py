from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# engine is the actual connection to your database
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # logs all SQL queries in development
    pool_size=5,  # max 5 permanent connections in the pool
    max_overflow=10,  # max 10 extra connections if pool is full
)

# SessionLocal is a factory that creates new DB sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# dependency — used in routes to get a db session
def get_db():
    db = SessionLocal()
    try:
        yield db  # give the session to the route
    finally:
        db.close()

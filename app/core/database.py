from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Retrieve the database URL from the settings
DATABASE_URL = settings.DATABASE_URL

# Create a new SQLAlchemy engine instance with connection pooling
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our classes definitions
Base = declarative_base()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

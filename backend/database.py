import os
from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Use SQLite for local development if PostgreSQL is not available
if not DATABASE_URL or DATABASE_URL.startswith("postgresql"):
    DATABASE_URL = "sqlite:///./todos.db"

engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

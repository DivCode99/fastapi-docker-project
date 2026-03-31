from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:Anubhav*1234@localhost:5432/fastapidb"

engine = create_engine(db_url)

session = sessionmaker(autoflush=False, autocommit=False,bind=engine)
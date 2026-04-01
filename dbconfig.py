from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:password@db:5432/fastapidb"

import time
from sqlalchemy import create_engine

for i in range(10):
    try:
        engine = create_engine(db_url)
        connection = engine.connect()
        print("DB Connected ✅")
        break
    except Exception as e:
        print("Waiting for DB... ⏳")
        time.sleep(2)

session = sessionmaker(autoflush=False, autocommit=False,bind=engine)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import dotenv
import os

dotenv.load_dotenv()

DB_PASSWORD = os.environ.get('DB_PASSWORD')
if DB_PASSWORD is None:
    print("DB_PASSWORD not found")

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
# SQLALCHEMY_DATABASE_URL = 'postgresql://admin:admin@localhost/TodoApplicationDatabase'
SQLALCHEMY_DATABASE_URL = f'postgresql://fastapi-todo-prod-db_owner:{DB_PASSWORD}@ep-square-band-a2xo5m8j.eu-central-1.aws.neon.tech/fastapi-todo-prod-db?sslmode=require'

engine = create_engine(SQLALCHEMY_DATABASE_URL) # FOR SQLITE: connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# storing details in local sqlite db for now
# since its running locally, i could do .ini, .property, .env etc for each connection and encrypt but think run-time file-based db may be better
# not much different than jupyter notebooks where people just store credentials openly in the editor anyhow :D 
DATABASE_URL = "sqlite:///./system.db" 

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

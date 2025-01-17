from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

from pydantic import BaseModel

# for initialization
class Conn(Base):
    __tablename__ = "connections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, index=True)
    host = Column(String, index=True)
    port = Column(Integer, index=True, nullable=True)
    sid = Column(String, index=True, nullable=True)
    svc_name = Column(String, index=True, nullable=True)
    dsn = Column(String, nullable=True)  # For Oracle (optional)
    driver = Column(String, nullable=True)  # For SQL Server (e.g., "ODBC Driver 17 for SQL Server")
    alt_conf = Column(String, index=True, nullable=True)
    description = Column(String, index=True, nullable=True)
    password = Column(String, index=True)
    ssl = Column(String, index=True, nullable=True)
# for post request
class ConnCreate(BaseModel):
    name: str
    type: str
    host: str
    port: int
    sid: str
    svc_name: str
    alt_conf: str
    description: str
    password: str
    ssl: str
    dsn: str
    driver: str
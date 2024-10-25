from sqlalchemy import Column, Integer, String
from .database import Base

from pydantic import BaseModel

# for initialization
class Conn(Base):
    __tablename__ = "connections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, index=True)
    host = Column(String, index=True)
    port = Column(Integer, index=True)
    sid = Column(String, index=True)
    svc_name = Column(String, index=True)
    alt_conf = Column(String, index=True)
    description = Column(String, index=True)
    password = Column(String, index=True)
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
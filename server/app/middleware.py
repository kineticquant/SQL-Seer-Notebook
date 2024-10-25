import os
import logging
from pathlib import Path
from sqlalchemy.orm import Session
from .models import Conn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# startup proc
current_dir = Path(__file__).resolve().parent
conf_dir = os.path.join(current_dir,'config')

def file_config():
    env_fi_exists = os.path.join(conf_dir, '.env')
    # connections_fi_exists = os.path.join(conf_dir, 'connections.ini')
    if not os.path.isfile(env_fi_exists):
        with open(env_fi_exists, 'w') as env:
            pass
        logger.info("Setup initialized for application.")
        logger.info("Created .env file.")
    # placed in sqlite instead of connections file
    # if not os.path.isfile(connections_fi_exists):
    #     with open(connections_fi_exists, 'w') as con_ini:
    #         pass
    #     logger.info("Created connections.ini file.")
    # connections_fi = os.path.join(conf_dir, 'connections.ini')
    # return connections_fi
 
def connections_config(db: Session):
    sqlite = db.query(Conn).filter(Conn.name == "System DB").first()
      
    if not sqlite:
        new_connection = Conn(
            name="System DB",
            type="sqlite",
            host="localhost",
            port=None,
            sid=None,
            svc_name=None,
            alt_conf=None,
            description="System Database",
            password=None
        )
        db.add(new_connection)
        logger.info("System database connection added.")
        db.commit()
    else:
        logger.info("System database configuration found.")
        
# end startup proc
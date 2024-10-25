import os
import logging
from pathlib import Path

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
    # if not os.path.isfile(connections_fi_exists):
    #     with open(connections_fi_exists, 'w') as con_ini:
    #         pass
    #     logger.info("Created connections.ini file.")
    # connections_fi = os.path.join(conf_dir, 'connections.ini')
    # return connections_fi
    
# end startup proc
from .models import Conn
from sqlalchemy.engine.url import URL
import os

DEFAULT_SQLITE_DB = "system.db"

# getting the connection URL's for the run query logic based on type of DB connection
# add SSL for cloud + secure connections
# oracle also handled separated with service names so 2 Oracle logic routes
def get_connection_url(conn: Conn) -> str:
    db_type = conn.type.lower()  # lowercase for case-insensitive comparison

    if db_type == "postgres":
        return URL.create(
            drivername="postgresql",
            username=conn.user,
            password=conn.password,
            host=conn.host,
            port=conn.port,
            database=conn.alt_conf,  # Use alt_conf for database name
        )
    elif db_type == "oracle":
        if conn.sid:
            return URL.create(
                drivername="oracle",
                username=conn.user,
                password=conn.password,
                host=conn.host,
                port=conn.port,
                database=conn.sid,
            )
        elif conn.svc_name:
            return URL.create(
                drivername="oracle",
                username=conn.user,
                password=conn.password,
                host=conn.host,
                port=conn.port,
                query={"service_name": conn.svc_name},
            )
        elif conn.dsn:
            return f"oracle://{conn.user}:{conn.password}@{conn.dsn}"
        else:
            raise ValueError("Oracle connection requires SID, service name, or DSN.")
    elif db_type == "sqlserver":
        return URL.create(
            drivername="mssql+pyodbc",
            username=conn.user,
            password=conn.password,
            host=conn.host,
            port=conn.port,
            database=conn.alt_conf,  
            query={"driver": conn.driver} if conn.driver else {},
        )
    elif db_type == "sqlite":
        sqlite_db = conn.alt_conf if conn.alt_conf else DEFAULT_SQLITE_DB
        sqlite_db_path = os.path.abspath(sqlite_db)
        return f"sqlite:///{sqlite_db_path}"  
    else:
        raise ValueError(f"Unsupported database type: {conn.type}")
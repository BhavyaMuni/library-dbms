from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import oracledb
from sshtunnel import SSHTunnelForwarder
from sqlalchemy.ext.declarative import declarative_base
import os

DIALECT = "oracle"
DBHOST = os.environ.get("ORACLE_HOST")
DBPORT = os.environ.get("ORACLE_PORT")
USERNAME = os.environ.get("ORACLE_USERNAME")  # enter your username
PASSWORD = os.environ.get("ORACLE_PASSWORD")  # enter your password
SID = oracledb.makedsn(
    "127.0.0.1", os.environ.get("LOCALPORT"), sid=os.environ.get("ORACLE_SID")
)

cstr = f"oracle+oracledb://{USERNAME}:{PASSWORD}@{SID}"
tunn = SSHTunnelForwarder(
    (os.environ.get("SSH_HOST"), 22),
    ssh_username=os.environ.get("SSH_USER"),
    ssh_password=os.environ.get("SSH_PASS"),
    remote_bind_address=(DBHOST, int(DBPORT)),
    local_bind_address=("0.0.0.0", int(os.environ.get("LOCALPORT"))),
)

tunn.start()

engine = create_engine(cstr)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

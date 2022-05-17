from time import time
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,MetaData,Table
from decouple import config
import json
from sqlalchemy.sql import text

DB_USER = 'bc_admin'
DB_PASSWORD = '7aff4f6e979711ec884a17a5405387ef'
DB_ADDRESS = 'venus.arz.team'
DB_NAME = 'blockchair'
DB_PORT = 5532

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_ADDRESS}:{DB_PORT}/{DB_NAME}", echo=False)
print('engine: ', engine)
engine.execution_options(stream_results=True)

meta = MetaData(bind=engine)
print('meta: ', meta)
meta.reflect(views=True)

blocks = meta.tables['blocks']
print('blocks: ', blocks)
transactions = meta.tables['transactions']


Session = sessionmaker(bind=engine)
print('Session: ', Session)
session = Session()
print('session: ', session)

res = session.query(blocks).order_by(blocks.c.time.desc()).limit(4)
print([data for data in res])

def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()



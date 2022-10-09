from ETL_db import *
from transform import *

session = sessionmaker(bind=engine)()


for user in users:
    row = Users(**user)
    session.add(row)
    
for upload in uploads:
    row = Uploads(**upload)
    session.add(row)

session.commit()
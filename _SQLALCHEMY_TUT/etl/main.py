
from ETL_db import *
session = sessionmaker(bind=engine)()

users = session.query(Users.UserId,Uploads.UploadId).join(Uploads,Users.UserId==Uploads.UserId,isouter=False).subquery().alias('Users')
# USERS = aliased(Users,users)
test = session.query(users).filter(users.c.UserId==1)



print("==>> users: ", users)
print("==>> test: ", test)
print("users",test.all())



from ETL_db import *
s = sessionmaker(bind=engine)()

users = s.query(Users.UserId,Uploads.UploadId).join(Uploads,Users.UserId==Uploads.UserId,isouter=False).subquery().alias('Users')
# USERS = aliased(Users,users)
test = s.query(users).filter(users.c.UserId==1)

a = s.query(Users).select_entity_from(Uploads).join(Users,isouter=True).all()
print("==>> a: ", a)

print("==>> users: ", users)
print("==>> test: ", test)
print("users",test.all())


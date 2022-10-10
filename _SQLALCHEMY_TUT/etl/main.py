
from ETL_db import *
s = sessionmaker(bind=engine)()

# users = s.query(Users.UserId,Uploads.UploadId).join(Uploads,Users.UserId==Uploads.UserId,isouter=False).subquery().alias("usr")
# # test = s.query(users).filter(users.c.UserId==1)

# a = s.query(Uploads).select_entity_from(users)
# print("==>> a: ", a)

# print("==>> a: ", a.all())

# print("==>> users: ", users)
# # print("==>> test: ", test)
# # print("users",test.all())


from sqlalchemy import *
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.sql import *

engine = create_engine('postgresql+psycopg2://root:1@arz.local:5432/')
Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    UserId = Column(Integer, primary_key=True)
    Title = Column(String)
    FirstName = Column(String)
    LastName = Column(String)
    Email = Column(String)
    Username = Column(String)
    DOB = Column(DateTime)
    # profile = relationship("Profile", back_populates='users')


class Uploads(Base):
    __tablename__ = "uploads"
    UploadId = Column(Integer, primary_key=True)
    UserId = Column(Integer)
    Title = Column(String)
    Body = Column(String)
    Timestamp = Column(DateTime)


class Profile(Base):
    __tablename__ = "profiles"
    Profile_id = Column(Integer, autoincrement=True, primary_key=True)
    # users_userid = Column(Integer, ForeignKey('users.UserId'))
    # users = relationship("Users", back_populates='profile')


Users.__table__.create(bind=engine, checkfirst=True)
Uploads.__table__.create(bind=engine, checkfirst=True)
Profile.__table__.create(bind=engine,checkfirst=True)
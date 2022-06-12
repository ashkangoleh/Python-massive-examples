from fastapi.responses import JSONResponse
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, FLOAT, func
from fastapi import Query, APIRouter
from datetime import datetime
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import BaseModel
import sqlalchemy

engine = create_engine(f"postgresql+psycopg2://data_scientist:ds_secret@venus.arz.team:5435/blocks", echo=False)
engine.execution_options(stream_results=True)
meta = MetaData(bind=engine)
meta.reflect(views=True)
Base = automap_base()
Base.prepare(engine, reflect=True)
bitcoin_capital = meta.tables['bitcoin_capital']

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

api = APIRouter()


def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$pbkdf2-sha256$29000$MsaY0/o/J2RsTWntXStl7A$Wz2fHCmgwo8TelGygvguD9jSW6/Q7aN2ywX.zxzjpP4",
        "disabled": False,
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)


# def get_password_hash(password):
#     return pwd_context.hash(password)


# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)


# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user


# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user


# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# @app.post("/token", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}


# @app.get("/users/me/", response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user


# @app.get("/users/me/items/")
# async def read_own_items(current_user: User = Depends(get_current_active_user)):
#     return [{"item_id": "Foo", "owner": current_user.username}]
from typing import Union
import datetime


# import decimal


# def decimal_default(obj):
#     if isinstance(obj, decimal.Decimal):
#         return float(obj)
#     raise TypeError

def query_hc(db, table_name, col_name, offset=1, limit=10, since='2009-01-03', until=str(datetime.datetime.now())):
    res = db.query(func.extract("EPOCH", table_name.c.time).label('time'),
                   getattr(table_name.columns, col_name).cast(FLOAT).label(col_name)).filter(
        table_name.c.time.between(since, until)).order_by(
        table_name.c.time.desc()).offset(offset).limit(limit)
    print('res: ', res)
    fa_num = '۰١٢٣٤٥٦٧٨٩'
    en_num = '0123456789'

    table = str.maketrans(en_num, fa_num)
    # normalized = "09912140491".translate(table)
    result = [(data.time, data[col_name]) for data in res]
    return result


def isinstance_expr(s, u):
    if isinstance(s, int) and isinstance(u, int):
        since = datetime.datetime.fromtimestamp(s)
        until = datetime.datetime.fromtimestamp(u)
    else:
        since = s
        until = u
    return since, until


@api.get('/test')
async def btc_cap_adjusted_price(page_num: int = 1, page_size: int = 10,
                                 s: Union[int, str] = Query(
                                     '2009-01-03', title="since", alias="since"),
                                 u: Union[int, str] = Query(
                                     str(datetime.datetime.now()), title="until", alias="until"),
                                 db: Session = Depends(get_db)):
    try:
        since, until = isinstance_expr(s, u)
        bcap = sqlalchemy.orm.aliased(bitcoin_capital, name='bcap')
        q = query_hc(db=db, table_name=bcap, col_name='price', offset=page_num, limit=page_size, since=since,
                     until=until)
        # print('res: ', res)
        # print('res: ', [data for data in res])
        print('res2: ', [data for data in q])
        response = {
            "status": "success",
            "message": "response returned successfully",
            "data": q,
        }
    except Exception as e:
        raise HTTPException(detail={
            "status": "failed",
            "message": "invalid parameters",
            "error": e
        }, status_code=status.HTTP_400_BAD_REQUEST)
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)

@api.get('/test1')
async def btc_cap_adjusted_price1(page_num: int = 1, page_size: int = 10,
                                 s: Union[int, str] = Query(
                                     '2009-01-03', title="since", alias="since"),
                                 u: Union[int, str] = Query(
                                     str(datetime.datetime.now()), title="until", alias="until"),
                                 db: Session = Depends(get_db)):
    try:
        since, until = isinstance_expr(s, u)
        bcap = sqlalchemy.orm.aliased(bitcoin_capital, name='bcap')
        q = query_hc(db=db, table_name=bcap, col_name='price', offset=page_num, limit=page_size, since=since,
                     until=until)
        # print('res: ', res)
        # print('res: ', [data for data in res])
        print('res2: ', [data for data in q])
        response = {
            "status": "success",
            "message": "response returned successfully",
            "data": q,
        }
    except Exception as e:
        raise HTTPException(detail={
            "status": "failed",
            "message": "invalid parameters",
            "error": e
        }, status_code=status.HTTP_400_BAD_REQUEST)
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
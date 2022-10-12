from typing import List, Union
from fastapi import Body, FastAPI, Header, Depends, Request

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from main import *
import uvicorn
from starlette_prometheus import metrics, PrometheusMiddleware

from starlette.requests import HTTPConnection

app = FastAPI()

app.add_middleware(PrometheusMiddleware)
app.add_route('/metrics', metrics)


class User(BaseModel):
    name: str
    token: str


fake_db = [
    User(name='foo', token='a1'),
    User(name='bar', token='a2')
]


async def get_user_by_token(token: str = Header()):
    for user in fake_db:
        if user.token == token:
            return user
        else:
            raise HTTPException(status_code=401, detail='Invalid token')


@app.get(path='/a', summary='Test route A')
async def test_route_a(user: User = Depends(get_user_by_token)):
    return user


@app.get(path='/b', summary='Test route B')
async def test_route_a(user: User = Depends(get_user_by_token)):
    return {'name': user.name}


@app.get('/1')
async def join_with_subquery():
    users = s.query(Users.UserId, Uploads.UploadId).join(
        Uploads, Users.UserId == Uploads.UserId, isouter=False).subquery().alias("usr")
    a = s.query(Uploads).select_entity_from(
        users).order_by(Uploads.UserId.desc()).all()
    return a


@app.get('/2')
async def with_query_params(id: int):
    users = s.query(Users, Uploads).join(
        Uploads, Users.UserId == Uploads.UserId, isouter=False).subquery().alias("usr")
    result = s.query(users).filter(users.c.UserId == id).all()
    return result


@app.post('/3')
async def with_body(req: dict = Body(...)):
    id = req.get('id', 1)

    users = s.query(Users, Uploads).join(
        Uploads, Users.UserId == Uploads.UserId, isouter=False).subquery().alias("usr")
    result = s.query(users).filter(users.c.UserId == id).all()
    return {
        "message": req.get("query", "Done"),
        "data": result
    }


@app.patch('/4')
async def patch_with_body(req: dict = Body(...)):
    id = req.get('id', 1)
    users = s.query(Users).filter(Users.UserId == id).first()
    users.FirstName = req.get('first_name')
    s.commit()
    return "Done"


@app.put('/5')
async def put_with_body(req: dict = Body(...)):
    id = req.get('id', 1)
    users = s.query(Users).filter(Users.UserId == id).first()
    users.FirstName = req.get('first_name', "ashkan")
    s.commit()
    return {
        "first_name": users.FirstName,
        "id": users.UserId
    }


@app.head('/6')
async def update_with_header(id: int | None = Header(default=None), first_name: str | None = Header(default=None)):
    users = s.query(Users).filter(Users.UserId == id).first()
    print("==>> id.as_integer_ratio(): ", id.bit_length())
    users.Title = first_name
    s.commit()
    return True


@app.options('/1')
async def options(req: dict = Body(...)):
    users = s.query(Users).filter(Users.UserId == req.get('id')).first()
    return users


@app.trace("/8")
async def trace_f(req: Request):
    for k, v in req.items():
        print(k)
        print(v)

    return True

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("fast:app", host="localhost",
                port=8080, debug=True, reload=True)

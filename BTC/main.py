from fastapi_pagination import Page, paginate, add_pagination, LimitOffsetPage
from fastapi import FastAPI, Depends
from matplotlib.pyplot import get
from pydantic import BaseModel
from block_statistics import Session, get_db, blockView


class User(BaseModel):
    name: str


app = FastAPI()


@app.get(
    "/",
    response_model=LimitOffsetPage[blockView],
)
async def route(db: Session = Depends(get)):
    result = db.query(blockView).filter(
        blockView.c.time >= 1230940800).filter(blockView.c.time <= 1648363800).order_by(blockView.c.height.desc())
    return paginate(result)


add_pagination(app)

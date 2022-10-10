from fastapi import FastAPI
from main import *
import uvicorn

app = FastAPI()


@app.get('/')
async def main():
    users = s.query(Users.UserId, Uploads.UploadId).join(
        Uploads, Users.UserId == Uploads.UserId, isouter=False).subquery().alias("usr")
    a = s.query(Uploads).select_entity_from(users).order_by(Uploads.UserId.desc()).all()
    return a


if __name__ == "__main__":
    uvicorn.run("fast:app", host="localhost",
                port=8080, debug=True, reload=True)

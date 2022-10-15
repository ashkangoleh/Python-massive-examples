from fastapi import BackgroundTasks, FastAPI
from fastapi.responses import JSONResponse
from celery_utils import create_celery, get_task_info
from workers import signature, AsyncResult
from pydantic import BaseModel
from pydantic.networks import EmailStr
import uvicorn


def create_app() -> FastAPI:
    current_app = FastAPI(title=" ",
                          description=" ",
                          version="1", )

    current_app.celery_app = create_celery()
    # current_app.include_router("_".router)
    return current_app


app = create_app()
celery = app.celery_app


class signUp(BaseModel):
    email: EmailStr


def send_email(email, message):
    print("==>> message: ", message)
    print("==>> email: ", email)


def on_raw_message(body):
    return body


@app.post("/sign-up", response_model=signUp)
async def signUp(data: signUp):
    task = signature("sign_up", kwargs={
                     "user_email": data.email}, queue="sign_up")
    result = task.apply_async()
    tk_id = result.id
    tk_state = result.state
    return JSONResponse(tk_id)


@app.get("/sign-in")
async def signUp(data):
    print("==>> data: ", data)
    print("Create User in database")
    task = signature("signing_in", kwargs={
                     "user_email": data}, queue="sign_in")
    print("==>> task: ", task)
    r = task.apply_async()
    # r = onboard_user.apply_async(kwargs={"user_email": data.email})
    # d = r.get(on_message=on_raw_message, propagate=False)
    d = r.result
    print("==>> d: ", d)
    return JSONResponse(content=d)


@app.get("/dash/{task_id}")
async def dashboard(task_id: str):
    result = get_task_info(task_id)

    return result


@app.get("/background-sign-up")
async def ping(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, "email@address.com", "Hi!")
    return {"message": "pong!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",
                port=8080, reload=True)

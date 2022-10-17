"""
FastAPI mini application that can be used to
interact with the API server and celery
"""
# from typing import Optional
from fastapi import BackgroundTasks, Body, FastAPI,status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from pydantic.networks import EmailStr
from pydantic.dataclasses import dataclass
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import Response
import uvicorn
from celery_utils import create_celery, get_task_info
from workers import signature, AsyncResult


def create_app() -> FastAPI:
    """
    Create app instance
    """
    current_app = FastAPI(title=" ",
                          description=" ",
                          version="1", )

    current_app.celery_app = create_celery()
    # current_app.include_router("_".router)
    return current_app


app = create_app()
celery = app.celery_app


@app.exception_handler(RequestValidationError)
async def http_exception_accept_handler(request: Request, exc: RequestValidationError) -> Response:
    raw_errors = exc.raw_errors
    error_wrapper = raw_errors[0]
    validation_error: ValidationError = error_wrapper.exc
    overwritten_errors = validation_error.errors()
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content={"detail": jsonable_encoder(
                            overwritten_errors)},
                        )


class Config:
    validate_assignment = True
    title = "sign up"
    error_msg_templates = {
        'value_error.email': 'value is not a valid email address!!!!',
    }
    schema_extra = {
        'examples': [
            {
                'email': 'a@a.com',
            }
        ]
    }


@dataclass(config=Config)
class SignUp:
    """Base model for sign up users

    Args:
        BM (BaseModel): model creation object
    """
    email: EmailStr


def send_email(email, message):
    """send email to users

    Args:
        email (str): parameters
        message (str): parameters
    """
    print("==>> message: ", message)
    print("==>> email: ", email)


def on_raw_message(body):
    """on raw message

    Args:
        body (dict): passing dictionary body

    Returns:
        dict: return message as dictionary
    """
    return body


@app.post("/sign-up", response_model=SignUp)
async def sign_up(data: SignUp):
    """
    sign up a user
    """
    task = signature("sign_up", kwargs={
                     "user_email": data.email}, queue="sign_up")
    result = task.apply_async()
    data = {}
    data[result.id] = result.state
    return JSONResponse(data)


@app.get("/sign-in")
async def sign_in(data):
    """
    sign in a user
    """
    task = signature("sign_in", kwargs={
                     "user_email": data}, queue="sign_in")
    result = task.apply_async()
    # r = onboard_user.apply_async(kwargs={"user_email": data.email})
    # d = r.get(on_message=on_raw_message, propagate=False)
    data = {}
    data[result.id] = result.state
    return JSONResponse(content=data)


@app.get("/dash/{task_id}")
async def dashboard(task_id: str):
    """Dashboard task

    Args:
        task_id (str): task identifier

    Returns:
        dict:  return results of dashboard
    """
    result = get_task_info(task_id)

    return result


# class Custom(BaseModel):
#     custom: Optional[int] = Field(None, max_length=1)


@app.post("/dash2")
async def dashboard2(task_id: str = Body(max_length=36),
                     custom: int = Body(gt=0, lt=10, embed=False)):
    """Dashboard task

    Args:
        task_id (str): task identifier

    Returns:
        dict:  return results of dashboard
    """
    result = get_task_info(task_id)

    return {
        "task_id": task_id,
        "result": result
    }


@app.get("/background-sign-up")
async def ping(background_tasks: BackgroundTasks):
    """Background tasks

    Args:
        background_tasks (BackgroundTasks): builtin background tasks

    Returns:
        dict: return dict with background tasks returned
    """
    background_tasks.add_task(send_email, "email@address.com", "Hi!")
    return {"message": "pong!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",
                port=8080, reload=True)

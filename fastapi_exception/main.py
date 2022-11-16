import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette import status
from fastapi.testclient import TestClient
from pydantic import BaseModel
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.exceptions import ExceptionMiddleware
from starlette.types import ASGIApp
app = FastAPI()


class PartnerAvailabilityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        raise CustomException(
            status.HTTP_503_SERVICE_UNAVAILABLE, 'Partner services is unavailable.'
        )
        return await call_next(request)


class UserData(BaseModel):
    pass


class PutUserData:
    def process(self, user_data):
        raise CustomException(404, 'Whatever')

# your code starts here


class CustomException(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


@app.put("/check")
def check(user_data: UserData):
    start = time.time()
    raise CustomException(5000500, "custom error message")
    # PutUserData().process(user_data)
    # print('\n'.join(["Web Method Completed", f"\tTotal Time: {time.time() - start}"]))
    # return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "OK"})


@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        # status_code=status.HTTP_400_BAD_REQUEST,
        content={"code": exc.code,
                 "message": f"Exception Occurred! Reason -> {exc.message}"},
    )


class PartnerAvailabilityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        raise CustomException(
            # status.HTTP_503_SERVICE_UNAVAILABLE,
            5000500,
            'Partner services is unavailable.'
        )
        return await call_next(request)


@app.middleware("http")
async def add_metric(request: Request, call_next):
    response = await call_next(request)
    print("Response: ", response.status_code)
    return response

# app.add_middleware(PartnerAvailabilityMiddleware)
# this is the change
app.add_middleware(ExceptionMiddleware, handlers=app.exception_handlers)
# # your code ends here

# tc = TestClient(app)

# response = tc.put('/check', json={})
# assert response.json()['message'].startswith('Exception Occurred!')  # this assertion passes

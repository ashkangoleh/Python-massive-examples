import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette import status
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI()


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
        # status_code=exc.code,
        content={"code": exc.code,
                 "message": f"Exception Occurred! Reason -> {exc.message}"},
    )


@app.middleware("http")
async def add_metric(request: Request, call_next):
    response = await call_next(request)
    print("Response: ", response.status_code)
    return response

# # your code ends here

# tc = TestClient(app)

# response = tc.put('/check', json={})
# assert response.json()['message'].startswith('Exception Occurred!')  # this assertion passes

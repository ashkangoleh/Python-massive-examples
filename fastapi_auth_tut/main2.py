from functools import wraps
from typing import Any, Callable, Optional
from fastapi import FastAPI, Form, Request, Path, Response, Header
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
app = FastAPI()
ORIGINS = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# auth_required decorator


def auth_required(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        try:
            response = requests.post(
                url="LOGIN_ENDPOINT",
                headers={
                    "Authorization": kwargs["authorization"],
                },
            )
            response.raise_for_status()
            return func(*args, **kwargs)
        except requests.HTTPError as error:
            return Response(
                status_code=error.response.status_code
            )

    return wrapper


@app.get("/info/")
@auth_required
def get_information(
    authorization: Optional[str] = Header(None)
) -> JSONResponse:
    return JSONResponse(content={"info": "The answer is 42."})


@app.post('/')
async def receiveLocationInfo(request: Request):
    result = await request.body()
    print('result: ', result)
    return result


if __name__ == '__main__':
    uvicorn.run('main2:app', host="localhost", port=7676, reload=True)

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.openapi.utils import get_openapi
import uvicorn
from api import api

from utils import get_code_samples

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "pbkdf2-sha256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
API_PREFIX = '/api/v1'

app = FastAPI()
app.include_router(router=api, prefix=API_PREFIX)


def custom_openapi():
    # cache the generated schema
    if app.openapi_schema:
        return app.openapi_schema

    # custom settings
    openapi_schema = get_openapi(
        title="Sample Project",
        version='0.0.1',
        routes=app.routes,
    )
    for route in app.routes:
        if route.path.startswith(API_PREFIX) and '.json' not in route.path:
            for method in route.methods:
                if method.lower() in openapi_schema["paths"][route.path]:
                    code_samples = get_code_samples(route=route, method=method)
                    openapi_schema["paths"][route.path][method.lower()]["x-codeSamples"] = code_samples

    app.openapi_schema = openapi_schema

    return app.openapi_schema


# assign the customized OpenAPI schema
app.openapi = custom_openapi

if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=7676, reload=True)

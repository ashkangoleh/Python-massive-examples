from fastapi import FastAPI, Form, Request, Path
import uvicorn
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
ORIGINS = ['*']
app.add_middleware(
            CORSMiddleware,
            allow_origins=ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


@app.post('/')
async def receiveLocationInfo(request: Request):
    result = await request.body()
    print('result: ', result)
    return result


if __name__ == '__main__':
    uvicorn.run('main2:app',host="localhost",port=7676,reload=True)
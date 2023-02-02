from fastapi import FastAPI, Query
import uvicorn
from routes import api

def application():
    """
    Create application
    """
    current_app = FastAPI()

    return current_app


app = application()
app.include_router(
    api,prefix="/api"
)

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)

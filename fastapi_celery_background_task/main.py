from fastapi import BackgroundTasks, FastAPI
from worker import onboard_user
from pydantic import BaseModel
from pydantic.networks import EmailStr
import uvicorn

app = FastAPI()


class signUp(BaseModel):
    email: EmailStr


def send_email(email, message):
    print("==>> message: ", message)
    print("==>> email: ", email)


@app.post("/sign-up", response_model=signUp)
async def signUp(data: signUp):
    print("Create User in database")
    onboard_user.apply_async(kwargs={"user_email": data.email})
    return data


@app.get("/background-sign-up")
async def ping(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, "email@address.com", "Hi!")
    return {"message": "pong!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",
                port=8080, reload=True)

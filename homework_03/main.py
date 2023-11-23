
import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping/")
def hw_ping():
    return {"message": "pong"}

@app.get("/login/{login}/{pwd}/")
def test_address(login: str, pwd: str):
    if login == 'user' and pwd == '123':
        return {"message": f"Hello {login}!!!"}
    else:
        return {"message": f"Login or Password incorrect!"}
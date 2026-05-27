from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI() 

class UserSignUp(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class Settings(BaseModel):
    app_name: str = "Chai App"
    admin_email: str = 'admin@chai.com'
    
def get_settings():
    return Settings()

@app.post("/signup")
def signup(user: UserSignUp):
    return {"message": f'User {user.username} signed up successfully'}

@app.get("/settings")
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings
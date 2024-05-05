from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from auth.database import User
from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager

router = APIRouter(
    prefix="",
    tags=["Pages"]
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


current_user = fastapi_users.current_user()
templates = Jinja2Templates(directory="template")

@router.get("/")
def get_main_page(request : Request):

    response = {
        "request" : request
    }
    
    return templates.TemplateResponse("index.html", response)

@router.get("/login")
def get_main_page(request : Request):

    response = {
        "request" : request
    }
    
    return templates.TemplateResponse("login.html", response)

@router.get("/register")
def get_main_page(request : Request):

    response = {
        "request" : request
    }
    
    return templates.TemplateResponse("register.html", response)


def get_main_page(request : Request):

    response = {
        "request" : request
    }
    
    return templates.TemplateResponse("register.html", response)


@router.get("/protected-main")
def protected_route(request : Request, user: User = Depends(current_user)):
    response = {
        "request" : request
    }
    
    return templates.TemplateResponse("main.html", response)
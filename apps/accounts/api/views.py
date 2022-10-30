from ninja import Router

from apps.accounts.api import schemas

from .. import services

router = Router()


@router.get("/status/")
def health_check(request):
    return {"status": "up"}


@router.post("/login/", response={200: schemas.Token, 401: schemas.Message})
def login(request, user: schemas.UserLoginSchema):
    token = services.login(**user.dict())
    return {"token": token}


@router.post("/signup/", response={200: schemas.UserSchema})
def signup(request, user_data: schemas.CreateUserSchema):
    # TODO: handle unique username errors
    user = services.signup(user_data.dict())
    return user

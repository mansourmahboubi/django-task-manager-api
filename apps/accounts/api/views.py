from ninja import Router

from apps.accounts.api import schema

from .. import services

router = Router()


@router.get("/status/")
def health_check(request):
    return {"status": "up"}


@router.post("/login/", response={200: schema.Token, 401: schema.Message})
def login(request, user: schema.UserSchema):
    token = services.login(**user.dict())
    return {"token": token}

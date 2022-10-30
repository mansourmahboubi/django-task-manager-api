from ninja import ModelSchema, Schema

from .. import models


class UserSchema(ModelSchema):
    # https://pydantic-docs.helpmanual.io/usage/types/
    # TODO: email validation can be added with email-validator
    class Config:
        model = models.User
        model_fields = ["username", "first_name", "last_name", "email"]


class CreateUserSchema(UserSchema):
    password: str


class UserNameSchema(Schema):
    username: str


class UserLoginSchema(UserNameSchema):
    password: str


class Token(Schema):
    token: str


class Message(Schema):
    detail: str

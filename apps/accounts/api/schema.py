from ninja import Schema


class UserSchema(Schema):
    username: str
    password: str


class Token(Schema):
    token: str


class Message(Schema):
    detail: str

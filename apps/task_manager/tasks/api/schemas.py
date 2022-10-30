from ninja import ModelSchema

from .. import models


class TaskSchema(ModelSchema):
    class Config:
        model = models.Task
        model_fields = ["id", "title", "created"]

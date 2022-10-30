from ninja import NinjaAPI

from apps.accounts.api.views import router as users_router
from apps.task_manager.tasks.api.views import router as tasks_router

api = NinjaAPI()

api.add_router("/", users_router)
api.add_router("/", tasks_router)

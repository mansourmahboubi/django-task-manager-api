from ninja import NinjaAPI
from ninja.security import APIKeyHeader

from apps.accounts.api.views import router as users_router
from apps.accounts.models import User
from apps.task_manager.tasks.api.views import router as tasks_router


class ApiKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        try:
            return User.objects.filter(token__isnull=False).get(token=key)
        except User.DoesNotExist:
            pass


api = NinjaAPI(auth=ApiKey())

api.add_router("/", users_router)
api.add_router("/", tasks_router)

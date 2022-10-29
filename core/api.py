from ninja import NinjaAPI

from apps.accounts.api.views import router as users_router

api = NinjaAPI()

api.add_router("/status/", users_router)

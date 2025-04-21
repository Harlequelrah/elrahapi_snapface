from .cruds import snapface_crud
from ..settings.auth.configs import authentication
from elrahapi.router.router_namespace import DefaultRoutesName, TypeRoute
from typing import List
from elrahapi.router.router_provider import CustomRouterProvider


router_provider = CustomRouterProvider(
    prefix="/snapfaces",
    tags=["snapface"],
    crud=snapface_crud,
    # authentication=authentication
)

public_routes_name:List[DefaultRoutesName]=[
    DefaultRoutesName.CREATE,
    DefaultRoutesName.READ_ALL,
    DefaultRoutesName.UPDATE,
    DefaultRoutesName.DELETE,
    DefaultRoutesName.PATCH,
    DefaultRoutesName.READ_ONE,
]
app_snapface = router_provider.get_custom_router(
    routes_name=public_routes_name
)


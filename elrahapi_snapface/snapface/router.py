from elrahapi.router.router_default_routes_name import DefaultRoutesName
from .cruds import snapface_crud
from typing import List

from elrahapi.router.router_provider import CustomRouterProvider

router_provider = CustomRouterProvider(
    prefix="/snapfaces",
    tags=["snapface"],
    crud=snapface_crud,
    
)
public_routes_name:List[DefaultRoutesName]=[
    DefaultRoutesName.CREATE,
    DefaultRoutesName.READ_ALL,
    DefaultRoutesName.UPDATE,
    DefaultRoutesName.DELETE,
    DefaultRoutesName.PATCH,
    DefaultRoutesName.READ_ONE,
]
app_snapface = router_provider.get_custom_public_router(
    public_routes_name=public_routes_name
)


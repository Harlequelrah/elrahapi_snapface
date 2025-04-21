from elrahapi.crud.crud_models import CrudModels
from .models import SnapFace  #remplacer par l'entité SQLAlchemy
from .schemas import SnapFaceCreateModel, SnapFaceUpdateModel,SnapFacePatchModel,SnapFacePydanticModel
from elrahapi.crud.crud_forgery import CrudForgery
from ..settings.database import session_manager


snapface_crud_models = CrudModels(
    entity_name="snapface",
    primary_key_name="id",  #remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=SnapFace, #remplacer par l'entité SQLAlchemy
    CreateModel=SnapFaceCreateModel, #Optionel
    UpdateModel=SnapFaceUpdateModel, #Optionel
    PatchModel=SnapFacePatchModel, #Optionel
    PydanticModel=SnapFacePydanticModel, #Optionel
)


snapface_crud = CrudForgery(
    crud_models=snapface_crud_models,
    session_manager=session_manager

)

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from datetime import datetime

class SnapFaceBaseModel(BaseModel):
    title:str=Field(example='Archibald à la plage')
    description:str=Field(example='Picnic à la plage')

class SnapFaceCreateModel(SnapFaceBaseModel):
    imageUrl:str=Field(example='assets/images/archibald_plate.jpg')
    location:Optional[str]=Field(example='Plage de Munich',default=None)

class SnapFaceUpdateModel(SnapFaceCreateModel):
    pass

class SnapFacePatchModel(BaseModel):
    title:Optional[str]=None
    description:Optional[str]=None
    imageUrl:Optional[str]=None
    snaps:Optional[int]=None
    createAt:Optional[datetime]=None
    location:Optional[str]=None

class SnapFacePydanticModel(SnapFaceCreateModel):
    id:int
    createdAt:datetime
    snaps:int
    class Config:
        from_attributes=True


from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, Union
from datetime import datetime
from ..utils.pyObject import PyObjectId


class Admin(BaseModel):
    class Config:
        orm_mode = True


class AddAdminModel(Admin):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    original_url: str = Field(...)
    identifier: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "original_url": "https://zoro.to/watch/naruto-shippuden-355?ep=8203",
                "identifier": "xAdjedjNa",
            }
        }

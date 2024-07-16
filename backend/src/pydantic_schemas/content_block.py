from pydantic import BaseModel
from typing import Optional
from db.models.course import ContentType


class ContentBlockBase(BaseModel):
    title: str
    description: Optional[str] = None
    type: ContentType
    url: Optional[str] = None
    content: Optional[str] = None
    section_id: int


class ContentBlockCreate(ContentBlockBase):
    pass


class ContentBlockUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[ContentType] = None
    url: Optional[str] = None
    content: Optional[str] = None

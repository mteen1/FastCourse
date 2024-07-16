from pydantic import BaseModel
from typing import Optional


class SectionBase(BaseModel):
    title: str
    description: Optional[str] = None
    course_id: int


class SectionCreate(SectionBase):
    pass


class SectionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

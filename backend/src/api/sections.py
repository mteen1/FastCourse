from typing import List

import fastapi
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.db_setup import get_db
from pydantic_schemas.section import SectionCreate, SectionUpdate
from pydantic_schemas.content_block import ContentBlockCreate
from api.utils.sections import (
    get_section,
    get_course_sections,
    create_section,
    update_section,
    delete_section,
    get_section_content_blocks
)

router = fastapi.APIRouter()

@router.get("/sections/{id}", response_model=SectionCreate)
async def read_section(id: int, db: Session = Depends(get_db)):
    db_section = get_section(db=db, section_id=id)
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return db_section

@router.get("/courses/{course_id}/sections", response_model=List[SectionCreate])
async def read_course_sections(course_id: int, db: Session = Depends(get_db)):
    sections = get_course_sections(db=db, course_id=course_id)
    if not sections:
        raise HTTPException(status_code=404, detail="No sections found")
    return sections

@router.post("/sections", response_model=SectionCreate)
async def create_new_section(section: SectionCreate, db: Session = Depends(get_db)):
    return create_section(db=db, section=section)

@router.patch("/sections/{id}", response_model=SectionCreate)
async def update_section_endpoint(id: int, section: SectionUpdate, db: Session = Depends(get_db)):
    db_section = update_section(db=db, section_id=id, section=section)
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return db_section

@router.delete("/sections/{id}", status_code=204)
async def delete_section_endpoint(id: int, db: Session = Depends(get_db)):
    db_section = delete_section(db=db, section_id=id)
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return None

@router.get("/sections/{section_id}/content-blocks", response_model=List[ContentBlockCreate])
async def read_section_content_blocks(section_id: int, db: Session = Depends(get_db)):
    content_blocks = get_section_content_blocks(db=db, section_id=section_id)
    if not content_blocks:
        raise HTTPException(status_code=404, detail="No content blocks found")
    return content_blocks

from typing import List

import fastapi
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.db_setup import get_db
from pydantic_schemas.content_block import ContentBlockCreate, ContentBlockCreate, ContentBlockUpdate
from api.utils.content_blocks import (
    get_content_block,
    create_content_block,
    update_content_block,
    delete_content_block
)

router = fastapi.APIRouter()

@router.get("/content-blocks/{id}", response_model=ContentBlockCreate)
async def read_content_block(id: int, db: Session = Depends(get_db)):
    db_content_block = get_content_block(db=db, content_block_id=id)
    if db_content_block is None:
        raise HTTPException(status_code=404, detail="Content block not found")
    return db_content_block

@router.post("/content-blocks", response_model=ContentBlockCreate)
async def create_new_content_block(content_block: ContentBlockCreate, db: Session = Depends(get_db)):
    return create_content_block(db=db, content_block=content_block)

@router.patch("/content-blocks/{id}", response_model=ContentBlockUpdate)
async def update_content_block_endpoint(id: int, content_block: ContentBlockUpdate, db: Session = Depends(get_db)):
    db_content_block = update_content_block(db=db, content_block_id=id, content_block=content_block)
    if db_content_block is None:
        raise HTTPException(status_code=404, detail="Content block not found")
    return db_content_block

@router.delete("/content-blocks/{id}", status_code=204)
async def delete_content_block_endpoint(id: int, db: Session = Depends(get_db)):
    db_content_block = delete_content_block(db=db, content_block_id=id)
    if db_content_block is None:
        raise HTTPException(status_code=404, detail="Content block not found")
    return None

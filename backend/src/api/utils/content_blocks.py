from sqlalchemy.orm import Session

from db.models.course import ContentBlock
from pydantic_schemas.content_block import ContentBlockCreate, ContentBlockUpdate


def get_content_block(db: Session, content_block_id: int):
    return db.query(ContentBlock).filter(ContentBlock.id == content_block_id).first()


def create_content_block(db: Session, content_block: ContentBlockCreate):
    db_content_block = ContentBlock(
        title=content_block.title,
        description=content_block.description,
        type=content_block.type,
        url=content_block.url,
        content=content_block.content,
        section_id=content_block.section_id,
    )
    db.add(db_content_block)
    db.commit()
    db.refresh(db_content_block)
    return db_content_block


def update_content_block(db: Session, content_block_id: int, content_block: ContentBlockUpdate):
    db_content_block = db.query(ContentBlock).filter(ContentBlock.id == content_block_id).first()
    if db_content_block:
        if content_block.title is not None:
            db_content_block.title = content_block.title
        if content_block.description is not None:
            db_content_block.description = content_block.description
        if content_block.type is not None:
            db_content_block.type = content_block.type
        if content_block.url is not None:
            db_content_block.url = content_block.url
        if content_block.content is not None:
            db_content_block.content = content_block.content
        db.commit()
        db.refresh(db_content_block)
    return db_content_block


def delete_content_block(db: Session, content_block_id: int):
    db_content_block = db.query(ContentBlock).filter(ContentBlock.id == content_block_id).first()
    if db_content_block:
        db.delete(db_content_block)
        db.commit()
    return db_content_block

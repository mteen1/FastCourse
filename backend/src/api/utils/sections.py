from sqlalchemy.orm import Session

from db.models.course import Section, ContentBlock
from pydantic_schemas.section import SectionCreate, SectionUpdate


def get_section(db: Session, section_id: int):
    return db.query(Section).filter(Section.id == section_id).first()


def get_course_sections(db: Session, course_id: int):
    return db.query(Section).filter(Section.course_id == course_id).all()


def create_section(db: Session, section: SectionCreate):
    db_section = Section(
        title=section.title,
        description=section.description,
        course_id=section.course_id,
    )
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section


def update_section(db: Session, section_id: int, section: SectionUpdate):
    db_section = db.query(Section).filter(Section.id == section_id).first()
    if db_section:
        db_section.title = section.title
        db_section.description = section.description
        db.commit()
        db.refresh(db_section)
    return db_section


def delete_section(db: Session, section_id: int):
    db_section = db.query(Section).filter(Section.id == section_id).first()
    if db_section:
        # Optionally, delete related content blocks first
        db.query(ContentBlock).filter(ContentBlock.section_id == section_id).delete()
        db.delete(db_section)
        db.commit()
    return db_section


def get_section_content_blocks(db: Session, section_id: int):
    return db.query(ContentBlock).filter(ContentBlock.section_id == section_id).all()


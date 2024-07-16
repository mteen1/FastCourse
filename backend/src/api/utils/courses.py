from sqlalchemy.orm import Session

from db.models.course import Course, Section
from pydantic_schemas.course import CourseCreate


def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def get_courses(db: Session):
    return db.query(Course).all()


def get_user_courses(db: Session, user_id: int):
    courses = db.query(Course).filter(Course.user_id == user_id).all()
    return courses


def create_course(db: Session, course: CourseCreate):
    db_course = Course(
        title=course.title,
        description=course.description,
        user_id=course.user_id,
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course:
        db.delete(db_course)
        db.commit()
    return db_course

def update_course(db: Session, course_id: int, course: CourseCreate):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    db_course.title = course.title
    db_course.description = course.description
    db.commit()
    db.refresh(db_course)
    return db_course

def read_sections(db: Session, course_id: int):
    return db.query(Section).filter(Section.course_id == course_id).all()
from fastapi import APIRouter, Query, Path
from typing import List, Optional
from app.services.course_service import CourseService
from app.schemas.course import ChapterDetail, Course, IndividualCourse

router = APIRouter()
course_service = CourseService()

@router.get("/courses", response_model=List[Course])
async def get_courses(
    sort_by: str = Query("alphabetical", enum=["alphabetical", "date", "rating"]),
    domain: Optional[str] = None
):
    return await course_service.get_courses(sort_by, domain)

@router.get("/courses/{course_id}", response_model=IndividualCourse)
async def get_course_overview(course_id: str = Path(...)):
    return await course_service.get_course_overview(course_id)

@router.get("/courses/{course_id}/chapters/{chapter_index}", response_model=ChapterDetail)
async def get_chapter_detail(
    course_id: str = Path(...),
    chapter_index: int = Path(...)
):
    return await course_service.get_chapter_detail(course_id, chapter_index)
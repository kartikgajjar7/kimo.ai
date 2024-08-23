from fastapi import APIRouter, Path, Body
from app.services.course_service import CourseService

router = APIRouter()
course_service = CourseService()

@router.post("/courses/{course_id}/chapters/{chapter_index}/rate")
async def rate_chapter(
    course_id: str = Path(...),
    chapter_index: int = Path(...),
    rating: bool = Body(...)
):
    return await course_service.rate_chapter(course_id, chapter_index, rating)
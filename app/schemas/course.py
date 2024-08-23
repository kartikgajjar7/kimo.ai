from pydantic import BaseModel, BeforeValidator, Field, ConfigDict
from typing import List, Annotated, Optional
from datetime import datetime

PyObjectId = Annotated[str, BeforeValidator(str)]

class ChapterBase(BaseModel):
    name: str
    text: str

class ChapterDetail(ChapterBase):
    positive_ratings: int
    negative_ratings: int

class Course(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    date: datetime
    description: str
    domain: List[str]
    total_rating: int
    rating_count:int
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )

class IndividualCourse(Course):
    chapters: List[ChapterDetail]

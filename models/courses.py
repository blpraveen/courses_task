from pydantic import BaseModel,Field
from utility import PyObjectId
from typing import List
from datetime import datetime

class ChapterModel(BaseModel):
     name: str
     text: str


class CourseModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    date: datetime
    description: str
    domain: List[str]
    chapters: List[ChapterModel]

    class Config:
        orm_mode = True




class CCRatingModel(BaseModel):
    user_id: PyObjectId = Field(default_factory=PyObjectId, alias="user_id")
    course_id: PyObjectId = Field(default_factory=PyObjectId, alias="course_id")
    chapter: int
    rate: int

    class Config:
        orm_mode = True



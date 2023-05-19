from fastapi import APIRouter
from models.courses import CCRatingModel
from schemas.courses import serializeDict,serializeList
from schemas.chapter import serializeChapterDict,serializeChapterList
from config.db import db_courses
from bson import ObjectId
import pymongo

course = APIRouter()

@course.get('/courses')
async def find_all_courses(sort: str = ''):
    if sort== "title":
        return serializeList(db_courses.courses.find().sort([("name", pymongo.ASCENDING)]))
    elif sort == "date":
        return serializeList(db_courses.courses.find().sort([("date", pymongo.DESCENDING)]))
    elif sort == "rating":
        return serializeList(db_courses.courses.find().sort([ ("rating", pymongo.DESCENDING)]))
    else: 
        return serializeList(db_courses.courses.find().sort([("name", pymongo.ASCENDING), ("date", pymongo.DESCENDING), ("rating", pymongo.DESCENDING)]))

@course.get('/course/{id}')
async def get_course(id):
    return serializeDict(db_courses.courses.find_one({"_id":ObjectId(id)}))


@course.get('/course/{id}/{chapter}')
async def get_course_chapter(id,chapter:int):
    course = db_courses.courses.find_one({"_id":ObjectId(id)})
    chap = course["chapters"][chapter]
    return serializeChapterDict(chap)

@course.get('/course_chapter/{id}/')
async def get_course_chapters(id):
    course = db_courses.courses.find_one({"_id":ObjectId(id)})
    return serializeChapterList(course["chapters"])


@course.post('/cc_rate')
async def create_ccrate(ccr: CCRatingModel):
    db_courses.cc_rate.update_one({"user_id":ccr.user_id,"course_id": ccr.course_id,"chapter":ccr.chapter} ,{"$setOnInsert":dict(ccr)},upsert=True)

    ## Computing Rating Percentage and update to course
    result = db_courses.cc_rate.aggregate([{"$match":{"course_id": ccr.course_id}},{"$count":"Total"}])
    total = 0
    if len(list(result)) > 0 :
        total = list(result)[0]['Total']
    positve = db_courses.cc_rate.aggregate([{"$match":{"course_id": ccr.course_id,"rate":1}},{"$count":"Count"}])
    count = 0
    if len(list(positve)) > 0:
        count = list(positve)[0]['Count']
    perc = 0 
    if total > 0:
        perc = round((count/total)*100)
    db_courses.cc_rate.update_one({"_id": ccr.course_id}, {"$set": {"rating": perc}})
    #####

    return serializeDict(db_courses.courses.find_one({"_id":ccr.course_id}))
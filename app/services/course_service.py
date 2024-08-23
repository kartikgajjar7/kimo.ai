from pymongo import MongoClient, ASCENDING, DESCENDING
from bson import ObjectId

class CourseService:
    def __init__(self):
        self.client = MongoClient('MONGODB_URL')
        self.db = self.client['course_database']
        self.courses = self.db['courses']

    async def get_courses(self, sort_by, domain=None):
        query = {}
        if domain:
            query['domain'] = domain

        if sort_by == 'alphabetical':
            sort = [('name', ASCENDING)]
        elif sort_by == 'date':
            sort = [('date', DESCENDING)]
        else:
            sort = [('total_rating', DESCENDING)]

        courses = self.courses.find(query).sort(sort)
        return list(courses)

    async def get_course_overview(self, course_id):
        return self.courses.find_one({'_id': ObjectId(course_id)})

    async def get_chapter_detail(self, course_id, chapter_index):
        course = self.courses.find_one({'_id': ObjectId(course_id)})
        if course and 0 <= chapter_index < len(course['chapters']):
            return course['chapters'][chapter_index]
        return None

    async def rate_chapter(self, course_id, chapter_index, rating):
        rating_field = 'chapters.{}.positive_ratings' if rating else 'chapters.{}.negative_ratings'
        rating_field = rating_field.format(chapter_index)

        result = self.courses.update_one(
            {'_id': ObjectId(course_id)},
            {'$inc': {rating_field: 1, 'rating_count': 1, 'total_rating': 1 if rating else -1}}
        )
        return {'success': result.modified_count > 0}
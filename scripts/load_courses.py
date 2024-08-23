import json
from pymongo import MongoClient
from datetime import datetime

def load_courses():
    client = MongoClient('MONGODB_URL')
    db = client['course_database']
    courses_collection = db['courses']

    courses_collection.create_index([("name", 1)])
    courses_collection.create_index([("date", -1)])
    courses_collection.create_index([("domain", 1)])

    with open('../data/courses.json', 'r') as file:
        courses = json.load(file)

    for course in courses:
        course['date'] = datetime.fromtimestamp(course['date'])
        course['total_rating'] = 0
        course['rating_count'] = 0
        for chapter in course['chapters']:
            chapter['positive_ratings'] = 0
            chapter['negative_ratings'] = 0

    courses_collection.insert_many(courses)

if __name__ == "__main__":
    load_courses()
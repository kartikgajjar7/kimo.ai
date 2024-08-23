from fastapi import FastAPI
from app.api.endpoints import courses, ratings

app = FastAPI()

app.include_router(courses.router)
app.include_router(ratings.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Course API",
            "endpoints":[
                "courses?sort_by=(rating||alphabetical||data)&domain=(ex=mathematics)",
                "courses/:courseID/",
                "courses/:courseID/chapters/:chapterIndex",
                "courses/:courseID/chapters/:chapterIndex/rate"]}

from fastapi import FastAPI
from routes import post, homePageData
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # Replace with your frontend URL (e.g., ["http://localhost:3000"])
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router, prefix="/api/v1")
app.include_router(homePageData.router, prefix="/api/v1")

from fastapi import APIRouter
from . import home_page_data, post

# Create an instance of the APIRouter class
router = APIRouter()

# Include the API routes
router.include_router(post.router, prefix="/posts")
router.include_router(home_page_data.router, prefix="/hpd")

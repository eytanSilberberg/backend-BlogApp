from fastapi import APIRouter, Depends, HTTPException
from models.post import Post, PostToSave, PostsResponse, PostResponse, ActionResponse
from db import get_database
from bson import ObjectId
from typing import List
import datetime

router = APIRouter()


# Custom Exception to handle database related errors
class DatabaseError(Exception):
    pass


# Custom Exception to handle 404 errors when a resource is not found
class NotFoundError(Exception):
    pass


# Function to convert the "_id" field of MongoDB to "id"
def convert_post(post):
    return {"id": str(post.pop("_id")), **post}


# Function to get a post by its ID, and raise exceptions accordingly
async def get_post_by_id(post_id: str, db):
    try:
        post = await db.post_dev.find_one({"_id": ObjectId(post_id)})
    except Exception as e:
        raise DatabaseError("Database error")
    if post is None:
        raise NotFoundError("Post not found")
    return post


# Route to create a new post
@router.post("/", response_model=ActionResponse)
async def create_post(post: PostToSave, db=Depends(get_database)):
    try:
        # Insert new post into the database
        inserted_post = await db.post_dev.insert_one(post.dict())
        post_id = inserted_post.inserted_id
        post = await db.post_dev.find_one({"_id": post_id})
        modified_post = convert_post(post)
    except DatabaseError:
        raise HTTPException(status_code=500, detail="Database error")
    return ActionResponse(data=modified_post, status="success")


# Route to get a specific post by ID
@router.get("/{post_id}", response_model=PostResponse)
async def read_post(post_id: str, db=Depends(get_database)):
    try:
        post = await get_post_by_id(post_id, db)
        modified_post = convert_post(post)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Post not found")
    return PostResponse(data=modified_post, status="success", timeStamp=datetime.datetime.now().timestamp())


# Route to update a specific post by ID
@router.put("/{post_id}", response_model=ActionResponse)
async def update_post(post_id: str, post: Post, db=Depends(get_database)):
    try:
        existing_post = await get_post_by_id(post_id, db)
        replika_post = {"title": post.title,
                        "description": post.description, "image": post.image}
        await db.post_dev.update_one({"_id": ObjectId(post_id)}, {"$set": replika_post})
        updated_post = await db.post_dev.find_one({"_id": ObjectId(post_id)})
        modified_post = convert_post(updated_post)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Post not found")
    return ActionResponse(data=modified_post, status="success")


# Route to delete a specific post by ID
@router.delete("/{post_id}", response_model=ActionResponse)
async def delete_post(post_id: str, db=Depends(get_database)):
    try:
        existing_post = await get_post_by_id(post_id, db)
        await db.post_dev.delete_one({"_id": ObjectId(post_id)})
        modified_post = convert_post(existing_post)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Post not found")
    return ActionResponse(data=modified_post, status="success")


# Route to get a list of all posts
@router.get("/", response_model=PostsResponse)
async def read_posts(db=Depends(get_database)):
    try:
        posts = await db.post_dev.find().to_list(length=None)
        modified_posts = [convert_post(post) for post in posts]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database error")
    return PostsResponse(data=modified_posts, status="success", timeStamp=datetime.datetime.now().timestamp())

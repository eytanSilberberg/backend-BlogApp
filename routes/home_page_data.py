from fastapi import APIRouter, Depends, HTTPException
from db import get_database
from models.home_page_data import HomePageDataResponse
import logging

router = APIRouter()

# Define route to fetch home page data with response model 'HomePageDataResponse'


@router.get("/", response_model=HomePageDataResponse)
async def read_home_page_data(db=Depends(get_database)):
    try:
        # Fetch the first document from 'homePageData' collection in the database
        homePageData = await db.homePageData.find_one({})
        print(homePageData)
        # Raise 404 if no home page data is found in the database
        if not homePageData:  # Added check for No Data
            raise HTTPException(
                status_code=404, detail="No Home Page Data Found")
         # Return fetched data with a 'success' status
        return HomePageDataResponse(data=homePageData, status="success")

    except Exception as e:
        # Changed from print to logging
        # Log error details and raise a 500 Internal Server Error
        logging.error(f"Failed to read home page data: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

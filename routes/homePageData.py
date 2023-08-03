from fastapi import APIRouter, Depends, HTTPException
from db import get_database
from models.homePageData import HomePageDataResponse

router = APIRouter()


@router.get("/hpd/", response_model=HomePageDataResponse)
async def read_posts(db=Depends(get_database)):
    try:
        homePageData = await db.homePageData.find().to_list(length=None)
        print(homePageData)
        modified_homePageData = homePageData[0]
        return HomePageDataResponse(**{"data": modified_homePageData, "status": "success"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

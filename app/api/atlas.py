from app.api.auth import get_api_key
from app.scraper.scrape import run

from fastapi import APIRouter, Depends, Query
from fastapi.security.api_key import APIKey

from typing import Union

router = APIRouter()

#TODO: Make the endpoints

#Get one zone by name
@router.get('/zone', summary='',
            response_model='',
            description="")
async def get_zone(
    x: Union[int, None] = None,
    api_key: APIKey = Depends(get_api_key),
):
    
    return t(t, t)

#Get path from zone A -> B
@router.get('/path', summary='',
            response_model='',
            description="")
async def get_path(
    x: Union[int, None] = None,
    api_key: APIKey = Depends(get_api_key),
):
    
    return t(t, t)

#Get all zones that match params
@router.get('/all', summary='',
            response_model='',
            description="")
async def get_all(
    x: Union[int, None] = Query(default=...),
    api_key: APIKey = Depends(get_api_key),
):
    
    return t(t, t)

#Rescrape (local) zone data
@router.get('/rescrape', summary='',
            response_model='',
            description="")
async def get_all(
    x: Union[int, None] = Query(default=...),
    api_key: APIKey = Depends(get_api_key),
):
    
    return run()
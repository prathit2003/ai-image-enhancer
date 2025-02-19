from fastapi import APIRouter
from services import get_image_url
router = APIRouter()

@router.get("/fetch_image/{public_id}") 
async def fetch_image(public_id : str): 
  image_url = get_image_url(public_id)
  return {"image_url" : image_url}
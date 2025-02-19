
from services import cloudinary  
from fastapi import HTTPException

def get_image_url(public_id: str) -> str:
    try:
        cloud_name = cloudinary.config().cloud_name
        if not cloud_name:
            raise HTTPException(status_code=500, detail="Cloudinary is not configured properly.")
        
        image_url = f"https://res.cloudinary.com/{cloud_name}/image/upload/{public_id}"
        return image_url

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


from services import cloudinary 
from fastapi import HTTPException
import cloudinary.uploader
from io import BytesIO
from PIL import Image


def upload_image(public_id:str, image_bytes: bytes) -> str: 
  try:
     
        image = Image.open(BytesIO(image_bytes))

        
        img_byte_array = BytesIO()
        image.save(img_byte_array, format="JPEG")
        img_byte_array.seek(0)

       
        upload_result = cloudinary.uploader.upload(
            img_byte_array,
            public_id=public_id,
            overwrite=True
        )

        return upload_result["secure_url"]
     
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))    
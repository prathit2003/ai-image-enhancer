from config.config import SetenvVar
import cloudinary


cloudinary.config(
    cloud_name=SetenvVar.CLOUDINARY_CLOUD_NAME,
    api_key=SetenvVar.CLOUDINARY_API_KEY,
    api_secret=SetenvVar.CLOUDINARY_API_SECRET
)

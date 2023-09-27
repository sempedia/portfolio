# cloudinary_config.py
import cloudinary
from cloudinary import uploader

cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

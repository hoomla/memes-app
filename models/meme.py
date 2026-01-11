from models.meme_image import MemeImage
from models.meme_source import MemeSource
from pydantic import BaseModel


class Meme(BaseModel):
    id: int
    description: str
    image: MemeImage
    rating: int | None = None
    source: MemeSource | None = None

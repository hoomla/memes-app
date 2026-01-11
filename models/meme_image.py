from pydantic import BaseModel, Field, HttpUrl


# Nested model for Meme
class MemeImage(BaseModel):
    url: HttpUrl = Field(..., examples=["https://example.com/meme.jpg"])
    width: int | None = Field(default=None, examples=[640])
    height: int | None = Field(default=None, examples=[480])

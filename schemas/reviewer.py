from typing import Optional
from pydantic import BaseModel, field

class reviewer(BaseModel):
    id: Optional[int] = None
    rev_name: str = field(max_length=15, min_length=3)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name":"Lynx Reviewer",
            }
        }
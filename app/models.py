from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class PlaceData(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    location: str = Field(index=True)
    data: dict  # JSON data you fetched from the external API
    updated_at: datetime = Field(default_factory=datetime.utcnow)

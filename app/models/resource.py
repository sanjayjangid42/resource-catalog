from datetime import datetime
from pydantic import BaseModel


class Resource(BaseModel):
    id: str
    name: str
    resource_type: str
    created_at: datetime
    updated_at: datetime

from pydantic import BaseModel, Field
from typing import Optional, List


class CreateResourceRequest(BaseModel):
    name: str = Field(..., min_length=1)
    resource_type: str = Field(..., min_length=1)


class UpdateResourceRequest(BaseModel):
    name: Optional[str] = None
    resource_type: Optional[str] = None


class ResourceResponse(BaseModel):
    data: dict


class ResourceListResponse(BaseModel):
    page: dict
    items: List[dict]

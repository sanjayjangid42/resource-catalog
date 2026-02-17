import uuid
import math
from datetime import datetime, timezone
from app.models.resource import Resource
from app.core.errors import AppException
from fastapi import APIRouter,Depends,Query
from app.repositories.resource_repository import ResourceRepository
from app.schemas.resource_schemas import CreateResourceRequest, UpdateResourceRequest

router = APIRouter()

# Dependency injector for repository
def get_repo():
    from app.main import repo  # Import the shared repo from main
    return repo


@router.get("/catalog/v1/resources")
def list_resources(
    _page: int = Query(1, ge=1),
    _items_per_page: int = Query(10, ge=1),
    resource_type: str | None = None,
    repo: ResourceRepository = Depends(get_repo)
):
    items = repo.list()

    if resource_type:
        items = [
            r for r in items
            if r.resource_type.lower() == resource_type.lower()
        ]

    total_items = len(items)
    total_pages = math.ceil(total_items / _items_per_page) if total_items else 0

    start = (_page - 1) * _items_per_page
    end = start + _items_per_page
    paginated = items[start:end]

    return {
        "page": {
            "total_items": total_items,
            "items_per_page": _items_per_page,
            "total_pages": total_pages,
            "current_page": _page,
            "has_next": _page < total_pages,
            "has_previous": _page > 1,
        },
        "items": paginated,
    }


@router.get("/catalog/v1/resources/{resource_id}")
def get_resource(resource_id: str,
                 repo: ResourceRepository = Depends(get_repo)):
    resource = repo.get(resource_id)
    if not resource:
        raise AppException(
            "RESOURCE_NOT_FOUND",
            f"No resource found with id '{resource_id}'.",
            404,
        )
    return {"data": resource}


@router.post("/catalog/v1/resources", status_code=201)
def create_resource(body: CreateResourceRequest,
                    repo: ResourceRepository = Depends(get_repo)):
    now = datetime.now(timezone.utc)
    resource = Resource(
        id=str(uuid.uuid4()),
        name=body.name,
        resource_type=body.resource_type,
        created_at=now,
        updated_at=now,
    )
    repo.create(resource)
    return {"data": resource}


@router.patch("/catalog/v1/resources/{resource_id}")
def update_resource(resource_id: str, body: UpdateResourceRequest,
                    repo: ResourceRepository = Depends(get_repo)):
    resource = repo.get(resource_id)
    if not resource:
        raise AppException(
            "RESOURCE_NOT_FOUND",
            f"No resource found with id '{resource_id}'.",
            404,
        )

    if body.name is not None:
        resource.name = body.name
    if body.resource_type is not None:
        resource.resource_type = body.resource_type

    resource.updated_at = datetime.now(timezone.utc)
    repo.create(resource)

    return {"data": resource}


@router.delete("/catalog/v1/resources/{resource_id}", status_code=204)
def delete_resource(resource_id: str,
                    repo: ResourceRepository = Depends(get_repo)):
    resource = repo.get(resource_id)
    if not resource:
        raise AppException(
            "RESOURCE_NOT_FOUND",
            f"No resource found with id '{resource_id}'.",
            404,
        )
    repo.delete(resource_id)

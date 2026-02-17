from typing import Dict, List, Optional
from app.models.resource import Resource
from uuid import uuid4
from datetime import datetime

class ResourceRepository:
    def __init__(self):
        self._storage: Dict[str, Resource] = {}

    def seed(self):
        """Seed 15 initial resources"""
        now = datetime.utcnow().isoformat()
        types = ["compute", "storage", "network"]
        for i in range(1, 16):
            r = Resource(
                id=str(uuid4()),
                name=f"resource-{i}",
                resource_type=types[i % 3],
                created_at=now,
                updated_at=now
            )
            self.create(r)

    def create(self, resource: Resource):
        self._storage[resource.id] = resource

    def get(self, resource_id: str) -> Optional[Resource]:
        return self._storage.get(resource_id)

    def list(self) -> List[Resource]:
        return list(self._storage.values())

    def delete(self, resource_id: str):
        self._storage.pop(resource_id, None)

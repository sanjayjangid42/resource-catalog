# Resource Catalog Microservice

A simple Python 3 microservice implementing a Resource Catalog with FastAPI.  
Supports CRUD operations, pagination, filtering, and includes a health endpoint.

---
## Features

- List, create, update, delete resources
- Pagination with `_page` and `_items_per_page`
- Filter resources by `resource_type` (case-insensitive)
- Health check endpoint (`/health`)
- Request ID included in every response (`X-Request-Id: rcat-<6hex>`)
- OpenAPI interactive docs: `/docs`
- In-memory storage (seeded with 15 resources at startup)
- Automated tests with `pytest`
- Dockerized for local development

---
## Requirements

- Python 3.11+
- uv (Python package manager) – https://github.com/astral-sh/uv
- Docker
- Docker Compose

---

## Installation

## 1. Clone the repository

git clone https://github.com/sanjayjangid42/resource-catalog.git

cd resource-catalog


# Local Setup (Using uv)

## 1. Install uv and dependencies

pip install uv

uv install

uv sync

## 2. Run tests

uv run pytest

---

## 3. Run the Service Locally

uv run uvicorn app.main:app --host 0.0.0.0 --port 8080

### _Service will be available at:_
http://localhost:8080

### _Interactive API documentation (Swagger UI):_
http://localhost:8080/docs

---

## 4. Run with Docker Compose

docker compose up --build

### The service will start on:
http://localhost:8080

### To stop the service:

docker compose down

## 5. Example curl commands


### 1. List Resources (Default Pagination)

curl http://localhost:8080/catalog/v1/resources

---

### 2. List Resources with Pagination

curl http://localhost:8080/catalog/v1/resources?_page=2&_items_per_page=5

---
### 3. Filter resources by type

curl http://localhost:8080/catalog/v1/resources?resource_type=compute

---
### 4. Get a single resource
curl http://localhost:8080/catalog/v1/resources/<resource_id>

---
### 5. Create a Resource

curl -X POST http://localhost:8080/catalog/v1/resources \
  -H "Content-Type: application/json" \
  -d '{"name":"example-server","resource_type":"compute"}'

---
### 6. Update a resource

curl -X PATCH http://localhost:8080/catalog/v1/resources/<resource_id> \
  -H "Content-Type: application/json" \
  -d '{"name":"updated-server","resource_type":"storage"}'

---
### 7. Delete a resource

curl -X DELETE http://localhost:8080/catalog/v1/resources/<resource_id>

---
### 8. Health Check

curl http://localhost:8080/health

Expected response:
{
  "status": "ok"
}

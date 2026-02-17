from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from contextlib import asynccontextmanager
from app.api.resources import router
from app.repositories.resource_repository import ResourceRepository
from app.core.errors import AppException, app_exception_handler, validation_exception_handler
from app.core.request_id import request_id_middleware

# Create a single repository instance
repo = ResourceRepository()


@asynccontextmanager
async def lifespan(app: FastAPI):
    #Seed 15 resources at startup
    repo.seed()
    yield


app = FastAPI(lifespan=lifespan, title= "Resources Catalog MicroService")

app.include_router(router)
app.middleware("http")(request_id_middleware)
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)



@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080)


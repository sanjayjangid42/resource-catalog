from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
import secrets

app = FastAPI(title="Resource Catalog")

# Middleware for X-Request-Id
@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = f"rcat-{secrets.token_hex(3)}"
    response = await call_next(request)
    response.headers["X-Request-Id"] = request_id
    return response

@app.get("/health")
def health():
    return {"status": "ok"}

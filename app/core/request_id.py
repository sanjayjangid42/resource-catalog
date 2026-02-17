import secrets
from fastapi import Request


async def request_id_middleware(request: Request, call_next):
    request_id = f"rcat-{secrets.token_hex(3)}"
    response = await call_next(request)
    response.headers["X-Request-Id"] = request_id
    return response

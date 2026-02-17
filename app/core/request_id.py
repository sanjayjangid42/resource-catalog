import secrets
from fastapi import Request


async def request_id_middleware(request: Request, call_next):
    request_id = f"rcat-{secrets.token_hex(3)}"

    # Store in request state so exception handlers can access it
    request.state.request_id = request_id

    response = await call_next(request)
    response.headers["X-Request-Id"] = request_id
    return response

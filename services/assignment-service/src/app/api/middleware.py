import logging
import uuid
from fastapi import Request

logger = logging.getLogger("assignment-service")


async def request_id_middleware(request: Request, call_next):
    rid = request.headers.get("X-Request-Id") or str(uuid.uuid4())
    request.state.request_id = rid

    response = await call_next(request)
    response.headers["X-Request-Id"] = rid

    logger.info("%s %s rid=%s status=%s",
                request.method, request.url.path, rid, response.status_code)
    return response

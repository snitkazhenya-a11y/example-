import time
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class TimingAndHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        request_id = str(uuid.uuid4())
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = f"{process_time:.4f} sec"
        response.headers["X-Process-ID"] = request_id
        return response
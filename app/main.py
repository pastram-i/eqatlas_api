import uuid
from typing import Awaitable, Callable

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from starlette.requests import Request
from starlette.responses import Response

from app import config
from app.api import api

app = FastAPI(
    title=config.TITLE,
    description=config.DESCRIPTION,
    version=config.VERSION,
    root_path=config.ROOT_PATH,
)

origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "https://localhost:8000",
    "https://localhost:8080",
    f"http://{config.URL}",
    f"https://{config.URL}",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def _request_middleware(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    request_id = str(uuid.uuid4())

    try:
        response = await call_next(request)
        # add security headers

    except Exception as ex:
        print(f"Request failed: {ex}")
        response = JSONResponse(content={"success": False}, status_code=500)

    finally:
        response.headers["X-Request-ID"] = request_id
        print("Request ended")
        return response
        

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    """Redirects root path to Swagger UI"""
    return RedirectResponse(url=f"{config.ROOT_PATH}docs")

app.include_router(api.router, prefix="/api")
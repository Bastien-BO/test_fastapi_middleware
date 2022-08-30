
from fastapi import Depends
from fastapi import FastAPI
from fastapi import Request
from fastapi.security import HTTPBasic, HTTPBearer
from fastapi.security.http import HTTPBase
#from fastapi.openapi.models import HTTPBase
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import JSONResponse
import uvicorn

from app.internal.depends.authorize import HTTPBaseLight
from app.internal.middlewares.auth import AuthBasicOrBearerBackend

app = FastAPI(
    dependencies=[
        Depends(HTTPBaseLight(scheme="basic")),
        Depends(HTTPBaseLight(scheme="bearer")),
    ],
    middleware=[
        Middleware(
            AuthenticationMiddleware,
            backend=AuthBasicOrBearerBackend(
                exclud_routes={"/docs", "/redoc", "/openapi.json"}
            ),
            on_error=lambda conn, exc: JSONResponse(
                {"detail": str(exc)}, status_code=401,
            ),
        ),
    ],

)


@app.get("/")
async def read_items(request: Request) -> str:
    return request.user.__dict__


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")

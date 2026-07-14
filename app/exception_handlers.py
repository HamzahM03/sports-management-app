from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions import OrganizationNotFoundError


async def organization_not_found_handler(
    request: Request,
    exc: OrganizationNotFoundError,
) -> JSONResponse:

    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)},
    )